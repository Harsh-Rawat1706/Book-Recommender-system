from flask import Flask, request , render_template
import pickle
import pandas as pd 
import numpy as np

app = Flask(__name__)

top50_books_df = pickle.load(open('top50_books.pkl', 'rb'))
similarity_score_df = pickle.load(open('similarity_score.pkl', 'rb'))  
pt_table_df = pickle.load(open('pt_table.pkl', 'rb'))
filtered_rate_book = pickle.load(open('filtered_rate_book.pkl', 'rb'))
@app.route('/')
def index():
    return render_template('index.html',
                           book_name = top50_books_df['Book-Title'].values,
                           author_name = top50_books_df['Book-Author'].values,
                           book_image = top50_books_df['Image-URL-M'].values,
                           book_rating = top50_books_df['avg_rating'].values
    )
    
@app.route("/recommend", methods=["GET"])
def recommend():
    return render_template("recommend.html")

@app.route("/recommend_books", methods=["POST"])
def recommend_books():
    user_input = request.form.get("user_input")
    if user_input not in pt_table_df.index:
        return render_template("recommend.html", error_message="Book is not present", recommended_books=None)
    # index fetching 
    index = np.where(pt_table_df.index == user_input)[0][0]
    distances = similarity_score_df[index]
    new_simi = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:11]  # skip the first (same book)

    recommended_books = []

    for i in new_simi:
        title = pt_table_df.index[i[0]]

        # Fetch the first matching book details
        details = filtered_rate_book[filtered_rate_book['Book-Title'] == title].iloc[0]

        recommended_books.append({
            'title': details['Book-Title'],
            'author': details['Book-Author'],
            'image_url': details['Image-URL-M']
        })
    print(recommended_books)
    return render_template("recommend.html", recommended_books=recommended_books)
if __name__ == '__main__':
    app.run(debug=True)