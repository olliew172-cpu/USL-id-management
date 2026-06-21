"""Vercel Serverless Function Entry Point"""
import os
import sys
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

load_dotenv()

from app import app

# Export the Flask app for Vercel
export = app
