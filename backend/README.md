# Backend

Run with `uvicorn app.main:app --reload` after installing `requirements.txt`. Test with `python -m pytest -q`.

The API never visits URLs found in messages and does not persist analyzed text.