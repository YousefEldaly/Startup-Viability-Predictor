from .OpenAI_API import OpenAI_API
from .GoogleSearch_API import GoogleSearch_API

get_response = OpenAI_API.get_response

__all__ = ["get_response"]