from fastapi import FastAPI, Form, HTTPException, Depends, status
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy.exc import IntegrityError
from passlib.context import CryptContext
from pydantic import EmailStr

# --------------------------------------------------
# DATABASE CONFIG
# --------------------------------------------------

DATABASE_URL = "postgresql://postgres:password@localhost:5432/tdb"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False
)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------------------------------------
# DATABASE MODEL
# --------------------------------------------------
class BankUser(Base):
    __tablename__ = "Bank_of_Spain"

    id = Column(Integer, primary_key=True, index=True)

    holder_name = Column(String(100), nullable=False)

    # IMPORTANT: account number is STRING, not INTEGER
    account_number = Column(String(10), unique=True, nullable=False)

    phone = Column(String(15), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)

Base.metadata.create_all(bind=engine)

# --------------------------------------------------
# SECURITY
# --------------------------------------------------
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# --------------------------------------------------
# FASTAPI APP
# --------------------------------------------------
app = FastAPI(
    title="Bank Signup API",
)

# --------------------------------------------------
# SIGNUP API
# --------------------------------------------------
@app.post("/signup")
def signup(
    holder_name: str = Form(...),
    account_number: str = Form(...),
    password: str = Form(...),
    phone: str = Form(...),
    email: EmailStr = Form(...),
    address: str = Form(...),
    db: Session = Depends(get_db)
):

    # ---------------- VALIDATIONS ----------------
    if not account_number.isdigit() or len(account_number) != 10:
        raise HTTPException(
            status_code=400,
            detail="Account number must be exactly 10 digits"
        )

    if len(password) < 8:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 8 characters"
        )

    if not phone.isdigit() or len(phone) not in (10, 11, 12):
        raise HTTPException(
            status_code=400,
            detail="Invalid phone number"
        )

    # ---------------- CREATE USER ----------------
    user = BankUser(
        holder_name=holder_name.strip(),
        account_number=account_number,
        phone=phone,
        email=email.lower(),
        password_hash=hash_password(password),
        address=address.strip()
    )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)

    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Account number, phone, or email already exists"
        )

    except Exception as e:
        db.rollback()
        print("ERROR:", e)
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )

    return {
        "message": "Account created successfully",
        "account_number": user.account_number,
        "holder_name": user.holder_name
    }
