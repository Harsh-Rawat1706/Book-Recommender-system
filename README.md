# 📚 Book Recommender System

This is a **Book Recommender System** built using **Flask**, **Python**, and **Cosine Similarity**. It provides a **Home Page** that displays the **Top 50 Books** and a **Recommendation Page** where you can search for a book and get the top 10 similar book recommendations.

## 🚀 Features
- Home Page displaying the Top 50 books from the dataset.
- Recommendation Page that takes a book name as input and recommends 10 similar books using cosine similarity.
- Shows “Book is not present” if the searched book is not found.
- Responsive UI using Bootstrap.
- Data stored in `.pkl` files for faster loading.

## 📂 Project Structure

├── myenv/ # Virtual environment

├── templates/ # HTML templates (Home, Recommend)

├── Requiements.txt # Python dependencies

├── app.py # Flask application

├── filtered_rate_book.pkl # Filtered book ratings data

├── pt_table.pkl # Pivot table for similarity

├── similarity_score.pkl # Precomputed similarity scores

├── top50_books.pkl # Data for top 50 books


## 🛠️ Installation & Setup
```bash
# 1️⃣ Clone the repository
git clone https://github.com/USERNAME/REPO_NAME.git](https://github.com/Harsh-Rawat1706/Book-Recommender-system.git
cd REPO_NAME

# 2️⃣ Create virtual environment
python -m venv myenv

# 3️⃣ Activate virtual environment
# Windows:
myenv\Scripts\activate
# Mac/Linux:
source myenv/bin/activate

# 4️⃣ Install dependencies
pip install -r Requiements.txt

# 5️⃣ Run the application
python app.py
```
# ⚙️ How It Works
Loads .pkl files containing book data, similarity scores, and pivot tables.

Uses cosine similarity on book ratings to find similar books.

Flask Routes:

1. / → Displays Top 50 books.

2. /recommend → Shows the recommendation search page.

3. /recommend_books → Processes search and shows recommendations.

# 📸 Screenshots
Home Page
<img width="1092" height="721" alt="Screenshot 2025-08-11 201107" src="https://github.com/user-attachments/assets/5464cba9-c91a-4221-9dbc-799aae1a23ed" />

Recommendation Page
<img width="1100" height="757" alt="Screenshot 2025-08-11 201134" src="https://github.com/user-attachments/assets/b213333e-2dc1-48a0-b8b5-c38bc34921f1" />

📌 Requirements
Main packages:

Flask

pandas

scikit-learn

pickle
(Full list in Requiements.txt)

🧑‍💻 Author
Your Name
📧 Email: hr9785771@gmail.com
🔗 GitHub: Harsh-Rawat1706
