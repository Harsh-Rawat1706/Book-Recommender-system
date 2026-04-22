import pickle
import pandas as pd 
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# ===== LOAD DATA =====
top50_books_df = pickle.load(open('top50_books.pkl', 'rb'))
similarity_score_df = pickle.load(open('similarity_score.pkl', 'rb'))  
pt_table_df = pickle.load(open('pt_table.pkl', 'rb'))
filtered_rate_book = pickle.load(open('filtered_rate_book.pkl', 'rb'))

# ===== HOME =====
@app.route('/')
def index():
    return render_template(
        'index.html',
        book_name=top50_books_df['Book-Title'].values,
        author_name=top50_books_df['Book-Author'].values,
        book_image=top50_books_df['Image-URL-M'].values,
        book_rating=top50_books_df['avg_rating'].values
    )

# ===== RECOMMEND PAGE =====
@app.route("/recommend", methods=["GET"])
def recommend():
    return render_template("recommend.html")

# ===== SMART SEARCH FUNCTION =====
def find_closest_book(user_input):
    user_input = user_input.lower().strip()

    # create lowercase index list
    all_books = pt_table_df.index.tolist()
    lower_books = [book.lower() for book in all_books]

    # find partial match
    matches = [i for i, book in enumerate(lower_books) if user_input in book]

    if matches:
        return all_books[matches[0]]  # return best match

    return None

# ===== RECOMMENDATION =====
@app.route("/recommend_books", methods=["POST"])
def recommend_books():
    user_input = request.form.get("user_input")

    if not user_input:
        return render_template(
            "recommend.html",
            error_message="Please enter a book name",
            recommended_books=None
        )

    # 🔥 smart matching
    matched_book = find_closest_book(user_input)

    if not matched_book:
        return render_template(
            "recommend.html",
            error_message="Book not known",
            recommended_books=None
        )

    # ===== GET INDEX =====
    index = np.where(pt_table_df.index == matched_book)[0][0]
    distances = similarity_score_df[index]

    new_simi = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:11]

    recommended_books = []

    for i in new_simi:
        title = pt_table_df.index[i[0]]

        details = filtered_rate_book[
            filtered_rate_book['Book-Title'] == title
        ].iloc[0]

        recommended_books.append({
            'title': details['Book-Title'],
            'author': details['Book-Author'],
            'image_url': details['Image-URL-M']
        })

    return render_template(
        "recommend.html",
        recommended_books=recommended_books,
        error_message=None
    )

# ===== RUN =====
if __name__ == '__main__':
    app.run(debug=True)