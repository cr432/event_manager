# Import necessary modules and functions from FastAPI and the standard library
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from app.dependencies import get_settings  # Custom configuration settings loader
from app.schemas.token_schemas import Token  # Import the Token schema from our application schemas
from app.utils.common import authenticate_user, create_access_token

# Load application settings
settings = get_settings()

# Initialize OAuth2PasswordBearer with the token URL
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create an API router object for registering endpoint(s)
router = APIRouter()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Endpoint to authenticate a user and issue an access token.
    
    Uses OAuth2PasswordRequestForm dependency to parse and validate the request form data (username and password).
    
    Args:
        form_data (OAuth2PasswordRequestForm): The form data containing the username and password.
        
    Returns:
        A JSON response containing the 'access_token' and 'token_type'.
    """
    
    # Authenticate the user with the provided credentials
    user = authenticate_user(form_data.username, form_data.password)
    
    # If authentication fails, differentiate between incorrect username and incorrect password
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Specify the duration the token will be valid
    access_token_expires = timedelta(minutes=settings.access_token_expire_minutes)
    
    # Generate an access token
    access_token = create_access_token(
        data={"sub": user["username"]},  # 'sub' (subject) field to identify the user
        expires_delta=access_token_expires
    )
    
    # Return the access token and token type to the client
    return {"access_token": access_token, "token_type": "bearer"}
