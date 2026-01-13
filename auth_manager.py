import streamlit as st
import json
import os
import hashlib

USER_DB_FILE = "users.json"

class AuthManager:
    def __init__(self):
        if 'logged_in' not in st.session_state:
            st.session_state['logged_in'] = False
        if 'current_user' not in st.session_state:
            st.session_state['current_user'] = None
        
        self.users = self._load_users()

    def _load_users(self):
        if not os.path.exists(USER_DB_FILE):
            # Default admin user if file doesn't exist
            # Storing hash of "admin" for simplicity in this demo, though ideally we salt.
            default_users = {"admin": self._hash_password("admin")}
            self._save_users(default_users)
            return default_users
        try:
            with open(USER_DB_FILE, 'r') as f:
                return json.load(f)
        except:
            return {}

    def _save_users(self, users):
        with open(USER_DB_FILE, 'w') as f:
            json.dump(users, f)

    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def is_logged_in(self):
        return st.session_state['logged_in']

    def login(self, username, password):
        hashed_pw = self._hash_password(password)
        if username in self.users and self.users[username] == hashed_pw:
            st.session_state['logged_in'] = True
            st.session_state['current_user'] = username
            return True
        return False

    def register(self, username, password):
        if username in self.users:
            return False, "Username already exists"
        
        self.users[username] = self._hash_password(password)
        self._save_users(self.users)
        # Auto-login after registration
        st.session_state['logged_in'] = True
        st.session_state['current_user'] = username
        return True, "User registered successfully"

    def logout(self):
        st.session_state['logged_in'] = False
        st.session_state['current_user'] = None

