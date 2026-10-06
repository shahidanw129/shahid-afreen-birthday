from flask import Flask, render_template, request, redirect, url_for, session
from functools import wraps

app = Flask(__name__)
app.secret_key = "shahid_afreen_birthday_secret_2026"

USERS = {"shahid": "1234"}

PAGE_DATA = {
    1: {
        "title": "Our Story",
        "eyebrow": "DECEMBER 2024 • THE BEGINNING",
        "heading": "From a Snapchat Add to Forever",
        "intro": "It started with a simple Snapchat add in December 2024. Somehow, that tiny notification became one of those little moments that turns into a beautiful friendship.",
        "images": [1,2,3,4,5,6],
        "captions": ["The first memories", "Two smiles, one story", "A beautiful beginning", "That effortless smile", "A moment worth keeping", "Little things, big memories"]
    },
    2: {
        "title": "Her Beautiful Moments",
        "eyebrow": "AFREEN • THE STAR OF THE STORY",
        "heading": "Every Picture Has a Story",
        "intro": "Some pictures are funny, some are calm, and some simply feel like Afreen. Every frame here is a tiny reminder of the person who made this friendship special.",
        "images": [7,8,9,10,11,12],
        "captions": ["Captured in the moment", "A classic mirror memory", "Simple & beautiful", "Old chats, old smiles", "That perfect pose", "Another favorite"]
    },
    3: {
        "title": "Shahid × Afreen",
        "eyebrow": "BEST FRIEND ENERGY",
        "heading": "Two People, One Unforgettable Friendship",
        "intro": "Shahid & Afreen — different personalities, random conversations, countless laughs, and a friendship that kept growing after that December 2024 Snapchat add.",
        "images": [13,14,15,16,17,18],
        "captions": ["Shahid's side of the story", "A mirror moment", "Smile mode: ON", "Soft memories", "Random but perfect", "Forever kind of vibe"]
    },
    4: {
        "title": "The Little Things",
        "eyebrow": "MEMORIES • LAUGHS • CHAOS",
        "heading": "It Is Always the Little Things",
        "intro": "The best friendships are not made only from big events. They grow through random selfies, silly poses, late conversations, inside jokes and the small moments nobody else understands.",
        "images": [19,20,21,22,23,24],
        "captions": ["That one expression", "Mirror magic", "Cute little details", "Main-character energy", "Dreamy moment", "Peaceful vibes"]
    },
    5: {
        "title": "A to Z",
        "eyebrow": "ONE LETTER • ONE MEMORY",
        "heading": "A to Z of Our Friendship",
        "intro": "A is for Awesome. B is for Bestie. C is for Caring. And somewhere between every letter is a memory that belongs to Shahid & Afreen.",
        "images": [25,26,27,28,29,30],
        "captions": ["A — Awesome", "B — Bestie", "C — Caring", "D — Dreamy", "E — Energetic", "F — Forever"]
    },
    6: {
        "title": "Birthday Messages",
        "eyebrow": "A LETTER FROM SHAHID",
        "heading": "Happy Birthday, Afreen ❤️",
        "intro": "May this new year of your life bring you peace, happiness, success and countless reasons to smile. Thank you for being such a special friend and for making ordinary days feel a little brighter.",
        "images": [31,32,33,34,35,36],
        "captions": ["Keep smiling", "A birthday glow", "Beautiful memories", "Stay exactly you", "Always shining", "Bestie forever"]
    },
    7: {
        "title": "Forever",
        "eyebrow": "THE LAST PAGE • NOT THE LAST MEMORY",
        "heading": "To More Years of Friendship",
        "intro": "From a Snapchat add in December 2024 to today — the story is still being written. Happy Birthday, Afreen. Whatever the next chapters bring, I hope they are full of happiness, laughter and beautiful memories.",
        "images": [36,37,38,39,40,41],
        "captions": ["One last birthday glow", "Still smiling", "Still making memories", "Still us", "One more favorite", "The story continues"]
    }
}
PHOTO_WISHES = {1: ['From that first little beginning, our friendship slowly became something genuinely special. Happy Birthday, Afreen — may every new chapter bring you more reasons to smile.', 'Some memories do not need a big occasion; they become precious simply because they belong to us. Wishing you a birthday as warm and beautiful as these moments.', 'December 2024 gave us a beginning, and every conversation after that added another page to the story. Happy Birthday, Afreen — keep shining exactly the way you do.', 'Your smile has a way of making an ordinary moment feel special. May this birthday bring you peaceful days, beautiful surprises and endless happiness.', 'A friendship can begin with one tiny notification and grow into countless memories. I am grateful for that beginning. Happy Birthday to an amazing bestie.', 'Here is to the first memories, the random moments and all the chapters still waiting for us. May your new year be full of laughter, success and beautiful people.'], 2: ['Every picture captures a different side of you, and every side deserves to be celebrated. Happy Birthday, Afreen — never forget how wonderfully unique you are.', 'Whether it is a mirror selfie or a completely random click, somehow you turn every frame into a memory worth keeping. Stay happy, stay confident, stay you.', 'Some photographs become favorites because of how they look; others become favorites because of how they make us feel. This one is definitely one of those memories.', 'May your birthday bring the same brightness that your smile brings into the lives of the people around you. Keep collecting beautiful moments.', 'A simple picture today becomes a story tomorrow. I hope your life keeps giving you stories that make you smile whenever you remember them.', 'Happy Birthday, Afreen. May every photo you take from this day forward capture a happier, stronger and more successful version of you.'], 3: ['Shahid × Afreen is a friendship made of random conversations, jokes, support and memories that somehow always become funnier with time.', 'No matter how simple the moment looks, friendship gives it meaning. Thank you for being one of those people who make ordinary days memorable.', 'Here is a little reminder that every friendship has its own language — ours is made of laughs, random talks, teasing and a lot of unforgettable moments.', 'Happy Birthday, Afreen. I hope you always have someone beside you who celebrates your wins, listens to your problems and laughs at your nonsense — and yes, I will try.', "Different moods, different days, same friendship. May the coming years give us even more reasons to look back and say, 'Those were the good days.'", 'To my bestie: may your life be filled with people who appreciate your heart, dreams that excite you and memories that never lose their magic.'], 4: ['The little things are often the biggest memories: random selfies, silly expressions, unexpected conversations and moments that were never planned.', 'Happy Birthday, Afreen. May you always find happiness in the small things and may the smallest moments become your biggest reasons to smile.', 'Every friendship has its own collection of inside jokes and random memories. These pictures are tiny pieces of ours, and I hope there are hundreds more to come.', 'You do not need a perfect day to create a beautiful memory. Sometimes a simple click, a laugh or a conversation is enough.', 'May your new year be full of peaceful mornings, exciting evenings, genuine smiles and people who make you feel valued exactly as you are.', 'Keep this little memory close: life changes, people grow, but the best moments stay with us. Happy Birthday, Afreen — here is to many more.'], 5: ['A — Awesome: because you have a way of making even normal conversations feel memorable. Happy Birthday, Afreen!', 'B — Bestie: because every great memory needs someone who can laugh with you, support you and still tolerate your random side.', 'C — Caring: because behind every joke and every fun moment is a heart that deserves the very best. May life always be kind to you.', "D — Dreamer: may you chase every dream fearlessly and turn every 'maybe someday' into a beautiful 'I did it.'", 'E — Energetic: may you keep your spark, your confidence and your beautiful energy through every new chapter of life.', 'F — Forever: not a promise that every day will be perfect, but a wish for a friendship filled with enough good memories to last forever.'], 6: ['Happy Birthday, Afreen! May your day be filled with genuine smiles, unexpected happiness, beautiful messages and the people who truly care about you.', 'On your birthday, I wish you success that makes you proud, peace that makes you calm and happiness that stays long after the celebrations end.', 'May every dream you are quietly working toward come closer this year. Believe in yourself — you are capable of much more than you realize.', 'Thank you for being part of so many random, funny and meaningful moments. Some friendships become memories; I hope ours keeps becoming a story.', 'Happy Birthday to a person whose smile deserves a thousand beautiful reasons to appear. Keep growing, keep glowing and keep being wonderfully you.', 'Today is your day, Afreen. Forget the stress, enjoy the moment, make a wish and remember that you deserve every good thing coming your way.'], 7: ['A birthday is not an ending; it is the beginning of another chapter. May this chapter of your life be your happiest and strongest one yet.', 'From December 2024 to today, so many little moments have become part of our story. I hope the future gives us even more memories to add.', 'No matter how much life changes, I hope we always have reasons to laugh at old memories and create completely new ones together.', 'May distance never make the good memories feel far away. Some friendships stay close because they live in the heart, not just in a place.', 'Here is to every chapter we have already lived and every chapter still waiting. Happy Birthday, Afreen — the best memories are still ahead.', 'The story does not end on this page. It continues with new birthdays, new adventures, new jokes and countless new memories. Shahid × Afreen, forever bestie energy.']}


def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        if not session.get("user"):
            return redirect(url_for("login"))
        return fn(*args, **kwargs)
    return wrapper

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip().lower()
        password = request.form.get("password", "")
        if USERS.get(username) == password:
            session["user"] = username
            return redirect(url_for("page", page_no=0))
        return render_template("login.html", error="Invalid username or password.")
    return render_template("login.html")

@app.route("/page/<int:page_no>")
@login_required
def page(page_no):
    if page_no == 0:
        return render_template("home.html", page_no=0)
    if page_no not in PAGE_DATA:
        return redirect(url_for("page", page_no=0))
    data = PAGE_DATA[page_no]
    return render_template("page.html", page_no=page_no, data=data, wishes=PHOTO_WISHES.get(page_no, []))

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

@app.route("/health")
def health():
    return {"status": "ok", "project": "Shahid × Afreen Birthday", "photos": 41}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
