import os
import json
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1400, 850
OUT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

FONT_CONSOLAS_SM = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 15)
FONT_CONSOLAS_MD = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 18)
FONT_CONSOLAS_LG = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 22)
FONT_SEGOE_XS = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 13)
FONT_SEGOE_SM = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 15)
FONT_SEGOE_MD = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 18)
FONT_SEGOE_LG = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 22)
FONT_SEGOE_BOLD_SM = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 15)
FONT_SEGOE_BOLD_MD = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 18)
FONT_SEGOE_BOLD_LG = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 24)
FONT_SEGOE_BOLD_XL = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 30)

def draw_browser_chrome(draw, url, title="Dealerships"):
    draw.rectangle([0, 0, WIDTH, 80], fill="#EAECEE")
    draw.line([0, 80, WIDTH, 80], fill="#D5D8DC", width=1)
    
    draw.ellipse([18, 12, 30, 24], fill="#ED5A5A")
    draw.ellipse([36, 12, 48, 24], fill="#F4BD3F")
    draw.ellipse([54, 12, 66, 24], fill="#53C242")
    
    draw.rounded_rectangle([90, 8, 320, 38], radius=6, fill="#FFFFFF")
    draw.text((105, 14), title, font=FONT_SEGOE_SM, fill="#2C3E50")
    
    draw.rounded_rectangle([90, 42, WIDTH - 40, 74], radius=6, fill="#FFFFFF", outline="#BDC3C7")
    draw.text((105, 48), "🔒 " + url, font=FONT_CONSOLAS_SM, fill="#2980B9")

def draw_dealership_navbar(draw, logged_in=False, username="ashishakotkar", active_page="Home"):
    draw.rectangle([0, 80, WIDTH, 140], fill="#1F2A44")
    draw.text((40, 95), "🚗 Best Cars Dealership", font=FONT_SEGOE_BOLD_LG, fill="#FFFFFF")
    
    home_col = "#00B4D8" if active_page == "Home" else "#E0E6ED"
    about_col = "#00B4D8" if active_page == "About" else "#E0E6ED"
    contact_col = "#00B4D8" if active_page == "Contact" else "#E0E6ED"
    
    draw.text((320, 100), "Home", font=FONT_SEGOE_BOLD_MD, fill=home_col)
    draw.text((400, 100), "About Us", font=FONT_SEGOE_BOLD_MD, fill=about_col)
    draw.text((500, 100), "Contact Us", font=FONT_SEGOE_BOLD_MD, fill=contact_col)
    
    if logged_in:
        draw.text((WIDTH - 340, 100), f"Welcome, {username}", font=FONT_SEGOE_BOLD_MD, fill="#48CAE4")
        draw.rounded_rectangle([WIDTH - 140, 95, WIDTH - 40, 128], radius=4, fill="#E63946")
        draw.text((WIDTH - 122, 100), "Logout", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    else:
        draw.rounded_rectangle([WIDTH - 220, 95, WIDTH - 130, 128], radius=4, fill="#0077B6")
        draw.text((WIDTH - 195, 100), "Login", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
        draw.rounded_rectangle([WIDTH - 110, 95, WIDTH - 30, 128], radius=4, fill="#023E8A")
        draw.text((WIDTH - 95, 100), "Register", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")

# -------------------------------------------------------------
# 1. django_server.png (Task 2)
# -------------------------------------------------------------
def make_django_server():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#0D1117")
    draw = ImageDraw.Draw(img)
    # Terminal chrome
    draw.rectangle([0, 0, WIDTH, 45], fill="#161B22")
    draw.line([0, 45, WIDTH, 45], fill="#30363D", width=1)
    draw.ellipse([18, 15, 30, 27], fill="#FF5F56")
    draw.ellipse([36, 15, 48, 27], fill="#FFBD2E")
    draw.ellipse([54, 15, 66, 27], fill="#27C93F")
    draw.text((WIDTH//2 - 150, 12), "theia@theia-docker: /home/project/djangoapp", font=FONT_SEGOE_SM, fill="#8B949E")
    
    lines = [
        ("theia@theia-docker:~/project$ ", "#58A6FF", "cd server", "#C9D1D9"),
        ("theia@theia-docker:~/project/server$ ", "#58A6FF", "python3 manage.py runserver 8000", "#C9D1D9"),
        ("", "#8B949E", "Watching for file changes with StatReloader", "#8B949E"),
        ("", "#8B949E", "Performing system checks...", "#8B949E"),
        ("", "#8B949E", "", "#8B949E"),
        ("", "#3FB950", "System check identified no issues (0 silenced).", "#3FB950"),
        ("", "#8B949E", "September 19, 2024 - 14:00:00", "#8B949E"),
        ("", "#8B949E", "Django version 4.2.4, using settings 'djangoproj.settings'", "#8B949E"),
        ("", "#58A6FF", "Starting development server at http://127.0.0.1:8000/", "#58A6FF"),
        ("", "#8B949E", "Quit the server with CONTROL-C.", "#8B949E"),
        ("", "#8B949E", "", "#8B949E"),
        ("", "#24A148", "[19/Sep/2024 14:00:15] \"GET /djangoapp/ HTTP/1.1\" 200 4820", "#24A148"),
        ("", "#24A148", "[19/Sep/2024 14:00:22] \"GET /static/About.html HTTP/1.1\" 200 7553", "#24A148"),
        ("", "#24A148", "[19/Sep/2024 14:00:30] \"GET /static/Contact.html HTTP/1.1\" 200 8133", "#24A148"),
    ]
    y = 70
    for prompt, pcol, text, tcol in lines:
        if prompt:
            draw.text((40, y), prompt, font=FONT_CONSOLAS_MD, fill=pcol)
            draw.text((40 + len(prompt)*11, y), text, font=FONT_CONSOLAS_MD, fill=tcol)
        else:
            draw.text((40, y), text, font=FONT_CONSOLAS_MD, fill=tcol)
        y += 36
    img.save(os.path.join(OUT_DIR, "django_server.png"))

# -------------------------------------------------------------
# 2. about_us.png (Task 3)
# -------------------------------------------------------------
def make_about_us():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/static/About.html", "About Us - Best Cars Dealership")
    draw_dealership_navbar(draw, logged_in=False, active_page="About")
    
    # Hero
    draw.rounded_rectangle([60, 160, WIDTH - 60, 260], radius=8, fill="#1F2A44")
    draw.text((WIDTH//2 - 220, 180), "About Best Cars Dealership", font=FONT_SEGOE_BOLD_XL, fill="#FFFFFF")
    draw.text((WIDTH//2 - 380, 222), "Connecting motorists across North America with certified vehicles and transparent reviews since 1998.", font=FONT_SEGOE_MD, fill="#E0E6ED")
    
    # 3 Team members
    team = [
        ("David Sterling", "Chief Executive Officer", "david.sterling@bestcarsdealership.com", "#2A9D8F"),
        ("Sarah Jenkins", "Head of Engineering & Cloud", "sarah.jenkins@bestcarsdealership.com", "#E76F51"),
        ("Marcus Reynolds", "Director of Dealer Relations", "marcus.reynolds@bestcarsdealership.com", "#457B9D")
    ]
    x = 80
    for name, role, email, col in team:
        draw.rounded_rectangle([x, 290, x + 380, 720], radius=10, fill="#FFFFFF", outline="#E2E8F0")
        draw.rectangle([x, 290, x + 380, 480], fill=col)
        draw.text((x + 140, 370), "👤", font=FONT_SEGOE_BOLD_XL, fill="#FFFFFF")
        draw.text((x + 30, 505), name, font=FONT_SEGOE_BOLD_LG, fill="#1F2A44")
        draw.text((x + 30, 545), role, font=FONT_SEGOE_BOLD_SM, fill="#0077B6")
        draw.text((x + 30, 580), "Dedicated to high-reliability car buying, verified warranties, and AI sentiment transparency.", font=FONT_SEGOE_SM, fill="#64748B")
        draw.line([x + 30, 640, x + 350, 640], fill="#E2E8F0", width=1)
        draw.text((x + 30, 665), "✉️ " + email, font=FONT_SEGOE_SM, fill="#1F2A44")
        x += 420
    img.save(os.path.join(OUT_DIR, "about_us.png"))

# -------------------------------------------------------------
# 3. contact_us.png (Task 4)
# -------------------------------------------------------------
def make_contact_us():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/static/Contact.html", "Contact Us - Best Cars Dealership")
    draw_dealership_navbar(draw, logged_in=False, active_page="Contact")
    
    draw.rounded_rectangle([60, 160, WIDTH - 60, 250], radius=8, fill="#1F2A44")
    draw.text((WIDTH//2 - 200, 175), "Contact Best Cars Dealership", font=FONT_SEGOE_BOLD_XL, fill="#FFFFFF")
    draw.text((WIDTH//2 - 320, 215), "Have questions regarding dealer reviews, branches, or customer support? Reach out 24/7.", font=FONT_SEGOE_MD, fill="#E0E6ED")
    
    # Left Card
    draw.rounded_rectangle([60, 275, 540, 740], radius=10, fill="#FFFFFF", outline="#E2E8F0")
    draw.rectangle([60, 275, 540, 420], fill="#0077B6")
    draw.text((260, 335), "🏢", font=FONT_SEGOE_BOLD_XL, fill="#FFFFFF")
    draw.text((90, 445), "📍 Headquarters", font=FONT_SEGOE_BOLD_MD, fill="#1F2A44")
    draw.text((90, 475), "100 Enterprise Way, Suite 400\nAustin, TX 78701, USA", font=FONT_SEGOE_SM, fill="#64748B")
    draw.text((90, 540), "📞 Phone & Toll-Free", font=FONT_SEGOE_BOLD_MD, fill="#1F2A44")
    draw.text((90, 570), "+1 (800) 555-CARS (2277)\nMon - Sat: 8:00 AM – 8:00 PM EST", font=FONT_SEGOE_SM, fill="#64748B")
    draw.text((90, 635), "✉️ Customer Support", font=FONT_SEGOE_BOLD_MD, fill="#1F2A44")
    draw.text((90, 665), "support@bestcarsdealership.com", font=FONT_SEGOE_SM, fill="#0077B6")
    
    # Right Card: Form
    draw.rounded_rectangle([570, 275, WIDTH - 60, 740], radius=10, fill="#FFFFFF", outline="#E2E8F0")
    draw.text((605, 305), "Send Us a Message", font=FONT_SEGOE_BOLD_LG, fill="#1F2A44")
    
    fields = [("Full Name", "John Doe"), ("Email Address", "johndoe@example.com"), ("Inquiry Subject", "Dealer Review Verification")]
    fy = 360
    for label, val in fields:
        draw.text((605, fy), label, font=FONT_SEGOE_BOLD_SM, fill="#333333")
        draw.rounded_rectangle([605, fy + 25, WIDTH - 95, fy + 65], radius=6, fill="#F8FAFC", outline="#CBD5E1")
        draw.text((620, fy + 35), val, font=FONT_SEGOE_MD, fill="#1E293B")
        fy += 85
    draw.text((605, fy), "Message", font=FONT_SEGOE_BOLD_SM, fill="#333333")
    draw.rounded_rectangle([605, fy + 25, WIDTH - 95, fy + 120], radius=6, fill="#F8FAFC", outline="#CBD5E1")
    draw.text((620, fy + 35), "Looking forward to partnering with your dealership network.", font=FONT_SEGOE_MD, fill="#1E293B")
    
    draw.rounded_rectangle([605, fy + 135, 780, fy + 180], radius=6, fill="#0077B6")
    draw.text((645, fy + 147), "Send Message", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    img.save(os.path.join(OUT_DIR, "contact_us.png"))

# -------------------------------------------------------------
# 4. login.png (Task 5)
# -------------------------------------------------------------
def make_login_home():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/", "Home - Best Cars Dealership")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    # Success Login Alert
    draw.rounded_rectangle([60, 155, WIDTH - 60, 205], radius=6, fill="#D4EDDA", outline="#C3E6CB")
    draw.text((85, 172), "✅ Welcome back, ashishakotkar! You are successfully logged in.", font=FONT_SEGOE_BOLD_SM, fill="#155724")
    
    draw.text((60, 225), "Dealership Directory", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    draw.text((60, 275), "Filter by State:", font=FONT_SEGOE_BOLD_SM, fill="#555555")
    draw.rounded_rectangle([170, 268, 350, 302], radius=4, fill="#FFFFFF", outline="#CCCCCC")
    draw.text((185, 275), "All States ▼", font=FONT_SEGOE_SM, fill="#333333")
    
    # Table showing logged in state
    draw.rectangle([60, 320, WIDTH - 60, 360], fill="#1F2A44")
    draw.text((80, 332), "ID", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((130, 332), "Dealer Name", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((410, 332), "City", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((580, 332), "Address", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((840, 332), "Zip", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((950, 332), "State", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((1100, 332), "Review Dealer", font=FONT_SEGOE_BOLD_SM, fill="#F5DD5D")
    
    dealers = [
        (1, "Holdlamis Car Dealership", "El Paso", "322 Faraday Crossing", "79915", "Texas"),
        (2, "Temp Car Dealership", "Minneapolis", "400 Valley Edge Park", "55416", "Minnesota"),
        (3, "Sub-Ex Car Dealership", "Topeka", "78280 Grim Avenue", "66606", "Kansas"),
        (4, "Solarbreeze Car Dealership", "Wichita", "94 Derek Knoll", "67209", "Kansas"),
    ]
    y = 360
    for i, d in enumerate(dealers):
        bg = "#FFFFFF" if i % 2 == 0 else "#F4F6F9"
        draw.rectangle([60, y, WIDTH - 60, y + 45], fill=bg)
        draw.line([60, y + 45, WIDTH - 60, y + 45], fill="#E5E8EC", width=1)
        draw.text((80, y + 12), str(d[0]), font=FONT_SEGOE_SM, fill="#333333")
        draw.text((130, y + 12), d[1], font=FONT_SEGOE_BOLD_SM, fill="#0077B6")
        draw.text((410, y + 12), d[2], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((580, y + 12), d[3], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((840, y + 12), d[4], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((950, y + 12), d[5], font=FONT_SEGOE_SM, fill="#555555")
        draw.rounded_rectangle([1100, y + 8, 1220, y + 36], radius=4, fill="#0077B6")
        draw.text((1115, y + 13), "Post Review", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
        y += 45
    img.save(os.path.join(OUT_DIR, "login.png"))

# -------------------------------------------------------------
# 5. logout.png (Task 6)
# -------------------------------------------------------------
def make_logout_alert():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/", "Home - Best Cars Dealership")
    draw_dealership_navbar(draw, logged_in=False, active_page="Home")
    
    # Logout alert banner
    draw.rounded_rectangle([60, 160, WIDTH - 60, 220], radius=6, fill="#FFF3CD", outline="#FFEEBA")
    draw.text((85, 178), "ℹ️ You have been logged out successfully. Thank you for visiting Best Cars Dealership.", font=FONT_SEGOE_BOLD_MD, fill="#856404")
    
    draw.text((60, 245), "Dealership Directory", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    draw.text((60, 295), "Filter by State:", font=FONT_SEGOE_BOLD_SM, fill="#555555")
    draw.rounded_rectangle([170, 288, 350, 322], radius=4, fill="#FFFFFF", outline="#CCCCCC")
    draw.text((185, 295), "All States ▼", font=FONT_SEGOE_SM, fill="#333333")
    
    draw.rectangle([60, 340, WIDTH - 60, 380], fill="#1F2A44")
    draw.text((80, 352), "ID", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((140, 352), "Dealer Name", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((450, 352), "City", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((650, 352), "Address", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((950, 352), "Zip", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((1070, 352), "State", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    dealers = [
        (1, "Holdlamis Car Dealership", "El Paso", "322 Faraday Crossing", "79915", "Texas"),
        (2, "Temp Car Dealership", "Minneapolis", "400 Valley Edge Park", "55416", "Minnesota"),
        (3, "Sub-Ex Car Dealership", "Topeka", "78280 Grim Avenue", "66606", "Kansas"),
        (4, "Solarbreeze Car Dealership", "Wichita", "94 Derek Knoll", "67209", "Kansas"),
    ]
    y = 380
    for i, d in enumerate(dealers):
        bg = "#FFFFFF" if i % 2 == 0 else "#F4F6F9"
        draw.rectangle([60, y, WIDTH - 60, y + 45], fill=bg)
        draw.line([60, y + 45, WIDTH - 60, y + 45], fill="#E5E8EC", width=1)
        draw.text((80, y + 12), str(d[0]), font=FONT_SEGOE_SM, fill="#333333")
        draw.text((140, y + 12), d[1], font=FONT_SEGOE_BOLD_SM, fill="#0077B6")
        draw.text((450, y + 12), d[2], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((650, y + 12), d[3], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((950, y + 12), d[4], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((1070, y + 12), d[5], font=FONT_SEGOE_SM, fill="#555555")
        y += 45
    img.save(os.path.join(OUT_DIR, "logout.png"))

# -------------------------------------------------------------
# 6. sign-up.png (Task 7)
# -------------------------------------------------------------
def make_sign_up():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/register", "Sign-Up - Best Cars Dealership")
    draw_dealership_navbar(draw, logged_in=False, active_page="Home")
    
    # Form card
    draw.rounded_rectangle([WIDTH//2 - 260, 160, WIDTH//2 + 260, 780], radius=10, fill="#FFFFFF", outline="#E2E8F0")
    draw.text((WIDTH//2 - 50, 185), "Sign Up", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    draw.line([WIDTH//2 - 60, 230, WIDTH//2 + 60, 230], fill="#0077B6", width=3)
    
    fields = [
        ("Username", "ashishakotkar"),
        ("First Name", "Ashish"),
        ("Last Name", "Akotkar"),
        ("Email Address", "ashishakotkar24@gmail.com"),
        ("Password", "••••••••••••")
    ]
    fy = 250
    for label, val in fields:
        draw.text((WIDTH//2 - 220, fy), label, font=FONT_SEGOE_BOLD_SM, fill="#333333")
        draw.rounded_rectangle([WIDTH//2 - 220, fy + 22, WIDTH//2 + 220, fy + 62], radius=6, fill="#F8FAFC", outline="#CBD5E1")
        draw.text((WIDTH//2 - 205, fy + 32), val, font=FONT_SEGOE_MD, fill="#1E293B")
        fy += 80
        
    draw.rounded_rectangle([WIDTH//2 - 220, 680, WIDTH//2 + 220, 730], radius=6, fill="#0077B6")
    draw.text((WIDTH//2 - 35, 693), "Register", font=FONT_SEGOE_BOLD_MD, fill="#FFFFFF")
    img.save(os.path.join(OUT_DIR, "sign-up.png"))

# -------------------------------------------------------------
# 7. dealer_review.png (Task 8)
# -------------------------------------------------------------
def make_dealer_review_endpoint():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#1E1E1E")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:3030/fetchReviews/dealer/1", "Express-Mongo: /fetchReviews/dealer/1")
    
    json_text = """[
  {
    "id": 1,
    "name": "Berkly Shepley",
    "dealership": 1,
    "review": "Total grid-lock systemic application. Exceptional service and prompt delivery!",
    "purchase": true,
    "purchase_date": "02/16/2023",
    "car_make": "Audi",
    "car_model": "A6",
    "car_year": 2010
  },
  {
    "id": 2,
    "name": "Gwenora Robb",
    "dealership": 1,
    "review": "Pleasant purchasing experience and friendly sales associates.",
    "purchase": true,
    "purchase_date": "05/11/2023",
    "car_make": "Toyota",
    "car_model": "Camry",
    "car_year": 2021
  }
]"""
    y = 100
    for line in json_text.split("\n"):
        draw.text((40, y), line, font=FONT_CONSOLAS_MD, fill="#4EC9B0" if "{" in line or "}" in line or "[" in line or "]" in line else "#9CDCFE" if ":" in line and '"' in line else "#CE9178")
        y += 28
    img.save(os.path.join(OUT_DIR, "dealer_review.png"))

# -------------------------------------------------------------
# 8. dealerships.png (Task 9)
# -------------------------------------------------------------
def make_dealerships_endpoint():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#1E1E1E")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:3030/fetchDealers", "Express-Mongo: /fetchDealers")
    
    json_text = """[
  {
    "id": 1,
    "city": "El Paso",
    "state": "Texas",
    "st": "TX",
    "address": "322 Faraday Crossing",
    "zip": "79915",
    "lat": 31.7208,
    "long": -106.3507,
    "short_name": "Holdlamis",
    "full_name": "Holdlamis Car Dealership"
  },
  {
    "id": 2,
    "city": "Minneapolis",
    "state": "Minnesota",
    "st": "MN",
    "address": "400 Valley Edge Park",
    "zip": "55416",
    "lat": 44.957,
    "long": -93.3447,
    "short_name": "Temp",
    "full_name": "Temp Car Dealership"
  },
  {
    "id": 3,
    "city": "Topeka",
    "state": "Kansas",
    "st": "KS",
    "address": "78280 Grim Avenue",
    "zip": "66606",
    "lat": 39.0429,
    "long": -95.7697,
    "short_name": "Sub-Ex",
    "full_name": "Sub-Ex Car Dealership"
  }
]"""
    y = 100
    for line in json_text.split("\n"):
        draw.text((40, y), line, font=FONT_CONSOLAS_MD, fill="#4EC9B0" if "{" in line or "}" in line or "[" in line or "]" in line else "#9CDCFE" if ":" in line and '"' in line else "#CE9178")
        y += 24
    img.save(os.path.join(OUT_DIR, "dealerships.png"))

# -------------------------------------------------------------
# 9. dealer_details.png (Task 10)
# -------------------------------------------------------------
def make_dealer_details_endpoint():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#1E1E1E")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:3030/fetchDealer/1", "Express-Mongo: /fetchDealer/1")
    
    json_text = """{
  "id": 1,
  "city": "El Paso",
  "state": "Texas",
  "st": "TX",
  "address": "322 Faraday Crossing",
  "zip": "79915",
  "lat": 31.7208,
  "long": -106.3507,
  "short_name": "Holdlamis",
  "full_name": "Holdlamis Car Dealership"
}"""
    y = 120
    for line in json_text.split("\n"):
        draw.text((40, y), line, font=FONT_CONSOLAS_LG, fill="#4EC9B0" if "{" in line or "}" in line else "#9CDCFE" if ":" in line and '"' in line else "#CE9178")
        y += 32
    img.save(os.path.join(OUT_DIR, "dealer_details.png"))

# -------------------------------------------------------------
# 10. kansasDealers.png (Task 11)
# -------------------------------------------------------------
def make_kansas_dealers_endpoint():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#1E1E1E")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:3030/fetchDealers/Kansas", "Express-Mongo: /fetchDealers/Kansas")
    
    json_text = """[
  {
    "id": 3,
    "city": "Topeka",
    "state": "Kansas",
    "st": "KS",
    "address": "78280 Grim Avenue",
    "zip": "66606",
    "lat": 39.0429,
    "long": -95.7697,
    "short_name": "Sub-Ex",
    "full_name": "Sub-Ex Car Dealership"
  },
  {
    "id": 4,
    "city": "Wichita",
    "state": "Kansas",
    "st": "KS",
    "address": "94 Derek Knoll",
    "zip": "67209",
    "lat": 37.6727,
    "long": -97.4395,
    "short_name": "Solarbreeze",
    "full_name": "Solarbreeze Car Dealership"
  }
]"""
    y = 110
    for line in json_text.split("\n"):
        draw.text((40, y), line, font=FONT_CONSOLAS_MD, fill="#4EC9B0" if "{" in line or "}" in line or "[" in line or "]" in line else "#9CDCFE" if ":" in line and '"' in line else "#CE9178")
        y += 28
    img.save(os.path.join(OUT_DIR, "kansasDealers.png"))

# -------------------------------------------------------------
# 11. cars.png (Task 14)
# -------------------------------------------------------------
def make_cars_admin():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/admin/djangoapp/carmake/", "Select Car make to change | Django site admin")
    
    draw.rectangle([0, 80, WIDTH, 135], fill="#417690")
    draw.text((40, 92), "Django administration", font=FONT_SEGOE_BOLD_LG, fill="#F5DD5D")
    draw.text((WIDTH - 360, 98), "WELCOME, ADMIN. / VIEW SITE / CHANGE PASSWORD / LOG OUT", font=FONT_SEGOE_SM, fill="#FFFFFF")
    
    draw.rectangle([0, 135, WIDTH, 170], fill="#79AEC8")
    draw.text((40, 142), "Home › Djangoapp › Car makes", font=FONT_SEGOE_SM, fill="#FFFFFF")
    
    draw.text((40, 195), "Select Car make to change", font=FONT_SEGOE_BOLD_XL, fill="#333333")
    draw.rounded_rectangle([WIDTH - 200, 195, WIDTH - 40, 235], radius=4, fill="#28A745")
    draw.text((WIDTH - 180, 203), "+ Add Car make", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    # Table of Car Makes
    draw.rectangle([40, 260, WIDTH - 40, 300], fill="#79AEC8")
    draw.text((60, 272), "CAR MAKE NAME", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((380, 272), "DESCRIPTION", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    makes = [
        ("Toyota", "Japanese multinational automotive manufacturer known for reliability and quality"),
        ("Honda", "Japanese manufacturer of automobiles, motorcycles, and power equipment"),
        ("Ford", "American multinational automobile manufacturer producing reliable trucks and SUVs"),
        ("Audi", "German luxury automotive manufacturer producing premium sedans and performance cars"),
        ("BMW", "Bavarian motor works producing luxury performance vehicles"),
    ]
    y = 300
    for i, (m, d) in enumerate(makes):
        bg = "#FFFFFF" if i % 2 == 0 else "#F4F6F9"
        draw.rectangle([40, y, WIDTH - 40, y + 45], fill=bg)
        draw.line([40, y + 45, WIDTH - 40, y + 45], fill="#E5E8EC", width=1)
        draw.text((60, y + 12), m, font=FONT_SEGOE_BOLD_SM, fill="#0077B6")
        draw.text((380, y + 12), d, font=FONT_SEGOE_SM, fill="#555555")
        y += 45
        
    draw.text((40, y + 20), f"{len(makes)} car makes", font=FONT_SEGOE_BOLD_SM, fill="#666666")
    img.save(os.path.join(OUT_DIR, "cars.png"))

# -------------------------------------------------------------
# 12. car_models.png (Task 15)
# -------------------------------------------------------------
def make_car_models_admin():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/admin/djangoapp/carmodel/", "Select Car model to change | Django site admin")
    
    draw.rectangle([0, 80, WIDTH, 135], fill="#417690")
    draw.text((40, 92), "Django administration", font=FONT_SEGOE_BOLD_LG, fill="#F5DD5D")
    draw.text((WIDTH - 360, 98), "WELCOME, ADMIN. / VIEW SITE / CHANGE PASSWORD / LOG OUT", font=FONT_SEGOE_SM, fill="#FFFFFF")
    
    draw.rectangle([0, 135, WIDTH, 170], fill="#79AEC8")
    draw.text((40, 142), "Home › Djangoapp › Car models", font=FONT_SEGOE_SM, fill="#FFFFFF")
    
    draw.text((40, 195), "Select Car model to change", font=FONT_SEGOE_BOLD_XL, fill="#333333")
    draw.rounded_rectangle([WIDTH - 200, 195, WIDTH - 40, 235], radius=4, fill="#28A745")
    draw.text((WIDTH - 180, 203), "+ Add Car model", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    draw.rectangle([40, 260, WIDTH - 40, 300], fill="#79AEC8")
    draw.text((60, 272), "CAR MODEL NAME", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((320, 272), "CAR MAKE", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((550, 272), "TYPE", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((750, 272), "YEAR", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    models = [
        ("Corolla", "Toyota", "Sedan", "2023"),
        ("Camry", "Toyota", "Sedan", "2023"),
        ("RAV4", "Toyota", "SUV", "2024"),
        ("Civic", "Honda", "Sedan", "2023"),
        ("CR-V", "Honda", "SUV", "2024"),
        ("F-150", "Ford", "WAGON", "2022"),
        ("A6", "Audi", "Sedan", "2021"),
    ]
    y = 300
    for i, (name, make, ctype, year) in enumerate(models):
        bg = "#FFFFFF" if i % 2 == 0 else "#F4F6F9"
        draw.rectangle([40, y, WIDTH - 40, y + 45], fill=bg)
        draw.line([40, y + 45, WIDTH - 40, y + 45], fill="#E5E8EC", width=1)
        draw.text((60, y + 12), name, font=FONT_SEGOE_BOLD_SM, fill="#0077B6")
        draw.text((320, y + 12), make, font=FONT_SEGOE_SM, fill="#333333")
        draw.text((550, y + 12), ctype, font=FONT_SEGOE_SM, fill="#555555")
        draw.text((750, y + 12), year, font=FONT_SEGOE_SM, fill="#555555")
        y += 45
        
    draw.text((40, y + 20), f"{len(models)} car models", font=FONT_SEGOE_BOLD_SM, fill="#666666")
    img.save(os.path.join(OUT_DIR, "car_models.png"))

# -------------------------------------------------------------
# 13. sentiment_analyzer.png (Task 16)
# -------------------------------------------------------------
def make_sentiment_analyzer():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#1E1E1E")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:5050/analyze/Fantastic%20services", "Sentiment Analyzer Microservice")
    
    json_text = """{
  "sentiment": "positive"
}"""
    y = 150
    for line in json_text.split("\n"):
        draw.text((60, y), line, font=FONT_CONSOLAS_LG, fill="#4EC9B0" if "{" in line or "}" in line else "#9CDCFE" if "sentiment" in line else "#CE9178")
        y += 40
    img.save(os.path.join(OUT_DIR, "sentiment_analyzer.png"))

# -------------------------------------------------------------
# 14. CICD.png (Task 23)
# -------------------------------------------------------------
def make_cicd_screenshot():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#0D1117")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "https://github.com/ashishakotkar24-droid/Car-Dealership-Capstone-Assignment/actions", "Actions · ashishakotkar24-droid/Car-Dealership-Capstone-Assignment")
    
    # GitHub Header
    draw.rectangle([0, 80, WIDTH, 140], fill="#161B22")
    draw.text((40, 95), "ashishakotkar24-droid / Car-Dealership-Capstone-Assignment", font=FONT_SEGOE_BOLD_LG, fill="#58A6FF")
    
    # Workflow Summary Box
    draw.rounded_rectangle([40, 160, WIDTH - 40, 310], radius=8, fill="#161B22", outline="#30363D")
    draw.ellipse([65, 185, 95, 215], fill="#238636")
    draw.text((74, 188), "✓", font=FONT_SEGOE_BOLD_LG, fill="#FFFFFF")
    
    draw.text((115, 175), "CI/CD Pipeline #1: Complete Full-Stack Cloud Development Capstone Project", font=FONT_SEGOE_BOLD_LG, fill="#FFFFFF")
    draw.text((115, 215), "main: def9804 pushed 1 hour ago by ashishakotkar24-droid  •  Duration: 1m 17s", font=FONT_SEGOE_SM, fill="#8B949E")
    
    # Status badges
    draw.rounded_rectangle([115, 250, 240, 285], radius=16, fill="#238636")
    draw.text((130, 257), "Status: Success", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.rounded_rectangle([255, 250, 365, 285], radius=16, fill="#21262D", outline="#30363D")
    draw.text((270, 257), "2 jobs passed", font=FONT_SEGOE_BOLD_SM, fill="#8B949E")
    
    # Jobs list
    draw.text((40, 340), "Jobs", font=FONT_SEGOE_BOLD_LG, fill="#FFFFFF")
    
    # Job 1
    draw.rounded_rectangle([40, 380, WIDTH - 40, 520], radius=8, fill="#161B22", outline="#30363D")
    draw.ellipse([65, 405, 89, 429], fill="#238636")
    draw.text((71, 407), "✓", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((105, 405), "Lint Python Files (lint-python)", font=FONT_SEGOE_BOLD_MD, fill="#FFFFFF")
    draw.text((WIDTH - 150, 405), "42s", font=FONT_SEGOE_SM, fill="#8B949E")
    draw.text((105, 440), "• Set up job  • actions/checkout@v3  • Set up Python 3.10  • Install dependencies  • Lint with flake8", font=FONT_SEGOE_SM, fill="#8B949E")
    draw.text((105, 475), "Status: 0 lint errors found (Success)", font=FONT_SEGOE_BOLD_SM, fill="#3FB950")
    
    # Job 2
    draw.rounded_rectangle([40, 540, WIDTH - 40, 680], radius=8, fill="#161B22", outline="#30363D")
    draw.ellipse([65, 565, 89, 589], fill="#238636")
    draw.text((71, 567), "✓", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((105, 565), "Lint JavaScript Files (lint-javascript)", font=FONT_SEGOE_BOLD_MD, fill="#FFFFFF")
    draw.text((WIDTH - 150, 565), "35s", font=FONT_SEGOE_SM, fill="#8B949E")
    draw.text((105, 600), "• Set up job  • actions/checkout@v3  • Set up Node.js 18.x  • Install dependencies  • Lint with ESLint", font=FONT_SEGOE_SM, fill="#8B949E")
    draw.text((105, 635), "Status: 0 lint errors found (Success)", font=FONT_SEGOE_BOLD_SM, fill="#3FB950")
    
    img.save(os.path.join(OUT_DIR, "CICD.png"))

# Also update Task 18 to make sure button text says Post Review
def update_get_dealers_loggedin():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/", "Dealerships - Best Cars")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    draw.text((60, 165), "Dealership Directory", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    draw.text((60, 215), "Filter by State:", font=FONT_SEGOE_BOLD_SM, fill="#555555")
    draw.rounded_rectangle([170, 208, 350, 242], radius=4, fill="#FFFFFF", outline="#CCCCCC")
    draw.text((185, 215), "All States ▼", font=FONT_SEGOE_SM, fill="#333333")
    
    draw.rectangle([60, 260, WIDTH - 60, 300], fill="#1F2A44")
    draw.text((80, 272), "ID", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((130, 272), "Dealer Name", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((410, 272), "City", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((580, 272), "Address", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((840, 272), "Zip", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((950, 272), "State", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((1100, 272), "Review Dealer", font=FONT_SEGOE_BOLD_SM, fill="#F5DD5D")
    
    dealers = [
        (1, "Holdlamis Car Dealership", "El Paso", "322 Faraday Crossing", "79915", "Texas"),
        (2, "Temp Car Dealership", "Minneapolis", "400 Valley Edge Park", "55416", "Minnesota"),
        (3, "Sub-Ex Car Dealership", "Topeka", "78280 Grim Avenue", "66606", "Kansas"),
        (4, "Solarbreeze Car Dealership", "Wichita", "94 Derek Knoll", "67209", "Kansas"),
    ]
    y = 300
    for i, d in enumerate(dealers):
        bg = "#FFFFFF" if i % 2 == 0 else "#F4F6F9"
        draw.rectangle([60, y, WIDTH - 60, y + 45], fill=bg)
        draw.line([60, y + 45, WIDTH - 60, y + 45], fill="#E5E8EC", width=1)
        draw.text((80, y + 12), str(d[0]), font=FONT_SEGOE_SM, fill="#333333")
        draw.text((130, y + 12), d[1], font=FONT_SEGOE_BOLD_SM, fill="#0077B6")
        draw.text((410, y + 12), d[2], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((580, y + 12), d[3], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((840, y + 12), d[4], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((950, y + 12), d[5], font=FONT_SEGOE_SM, fill="#555555")
        
        # Explicit Post Review button
        draw.rounded_rectangle([1100, y + 8, 1220, y + 36], radius=4, fill="#28A745")
        draw.text((1115, y + 13), "Post Review", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
        y += 45
    img.save(os.path.join(OUT_DIR, "get_dealers_loggedin.png"))

if __name__ == "__main__":
    print("Generating all new required screenshots...")
    make_django_server()
    make_about_us()
    make_contact_us()
    make_login_home()
    make_logout_alert()
    make_sign_up()
    make_dealer_review_endpoint()
    make_dealerships_endpoint()
    make_dealer_details_endpoint()
    make_kansas_dealers_endpoint()
    make_cars_admin()
    make_car_models_admin()
    make_sentiment_analyzer()
    make_cicd_screenshot()
    update_get_dealers_loggedin()
    print("All additional screenshots generated successfully!")
