# Shahid × Afreen — Bestie Forever

Premium Flask birthday/memory website built around the supplied 41-page photo PDF.

## Features
- Login page first
- Login: `shahid` / `1234`
- Home + 7 individual pages
- One-click page navigation: only the selected page is shown
- All 41 supplied photo pages extracted into `static/images`
- 6-photo layout on Pages 1–6; Page 7 shows all remaining photos plus a final story card
- Responsive desktop + mobile design
- Premium glassmorphism, gradients, animations and photo lightbox
- Flask session login
- No database required
- Works locally and is deployment-ready

## Run on Windows
1. Install Python 3.10+.
2. Open Command Prompt in this folder.
3. Run:
   `python -m venv venv`
4. Activate:
   `venv\\Scripts\\activate`
5. Install:
   `pip install -r requirements.txt`
6. Start:
   `python app.py`
7. Open:
   `http://127.0.0.1:5000`

## Login
Username: `shahid`
Password: `1234`

## Deploy
The app listens on `0.0.0.0` and uses port `5000` locally. For platforms that provide a `$PORT` variable, change the final line in `app.py` to:
`app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))`
and add `import os`.

For production, use a strong random Flask secret key and real authentication credentials.
