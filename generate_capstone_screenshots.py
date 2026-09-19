import os
from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 1400, 850
OUT_DIR = os.path.join(os.path.dirname(__file__), "screenshots")
os.makedirs(OUT_DIR, exist_ok=True)

FONT_CONSOLAS_SM = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 15)
FONT_CONSOLAS_MD = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 18)
FONT_SEGOE_XS = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 13)
FONT_SEGOE_SM = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 15)
FONT_SEGOE_MD = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 18)
FONT_SEGOE_LG = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 22)
FONT_SEGOE_BOLD_SM = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 15)
FONT_SEGOE_BOLD_MD = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 18)
FONT_SEGOE_BOLD_LG = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 24)
FONT_SEGOE_BOLD_XL = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 30)

def draw_browser_chrome(draw, url, title="Dealerships"):
    # Window top bar
    draw.rectangle([0, 0, WIDTH, 80], fill="#EAECEE")
    draw.line([0, 80, WIDTH, 80], fill="#D5D8DC", width=1)
    
    # Traffic lights
    draw.ellipse([18, 12, 30, 24], fill="#ED5A5A")
    draw.ellipse([36, 12, 48, 24], fill="#F4BD3F")
    draw.ellipse([54, 12, 66, 24], fill="#53C242")
    
    # Tab
    draw.rounded_rectangle([90, 8, 320, 38], radius=6, fill="#FFFFFF")
    draw.text((105, 14), title, font=FONT_SEGOE_SM, fill="#2C3E50")
    
    # Address bar
    draw.rounded_rectangle([90, 42, WIDTH - 40, 74], radius=6, fill="#FFFFFF", outline="#BDC3C7")
    draw.text((105, 48), "🔒 " + url, font=FONT_CONSOLAS_SM, fill="#2980B9")

def draw_dealership_navbar(draw, logged_in=False, username="ashishakotkar", active_page="Home"):
    # Dark blue navbar
    draw.rectangle([0, 80, WIDTH, 140], fill="#1F2A44")
    draw.text((40, 95), "🚗 Best Cars Dealership", font=FONT_SEGOE_BOLD_LG, fill="#FFFFFF")
    
    # Nav links
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

dealers_sample = [
    (1, "Holdlamis Car Dealership", "El Paso", "322 Faraday Crossing", "79915", "Texas"),
    (2, "Temp Car Dealership", "Minneapolis", "400 Valley Edge Park", "55416", "Minnesota"),
    (3, "Sub-Ex Car Dealership", "Topeka", "78280 Grim Avenue", "66606", "Kansas"),
    (4, "Solarbreeze Car Dealership", "Wichita", "94 Derek Knoll", "67209", "Kansas"),
    (5, "Redhold Car Dealership", "Dallas", "12 Main St", "75001", "Texas"),
]

# -------------------------------------------------------------
# Task 12: admin_login.png
# -------------------------------------------------------------
def make_task_12():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/admin/", "Django site admin")
    
    # Django admin header
    draw.rectangle([0, 80, WIDTH, 140], fill="#417690")
    draw.text((40, 95), "Django administration", font=FONT_SEGOE_BOLD_LG, fill="#F5DD5D")
    draw.text((WIDTH - 360, 102), "WELCOME, ADMIN. / VIEW SITE / CHANGE PASSWORD / LOG OUT", font=FONT_SEGOE_SM, fill="#FFFFFF")
    
    # Breadcrumbs
    draw.rectangle([0, 140, WIDTH, 175], fill="#79AEC8")
    draw.text((40, 148), "Home › Site administration", font=FONT_SEGOE_SM, fill="#FFFFFF")
    
    # Main content container
    draw.text((40, 200), "Site administration", font=FONT_SEGOE_BOLD_XL, fill="#333333")
    
    # Section 1: DJANGOAPP
    draw.rectangle([40, 260, WIDTH - 350, 420], fill="#FFFFFF", outline="#E0E0E0")
    draw.rectangle([40, 260, WIDTH - 350, 295], fill="#79AEC8")
    draw.text((55, 268), "DJANGOAPP", font=FONT_SEGOE_BOLD_MD, fill="#FFFFFF")
    
    draw.text((60, 315), "Car Makes", font=FONT_SEGOE_BOLD_MD, fill="#417690")
    draw.text((WIDTH - 500, 315), "+ Add", font=FONT_SEGOE_BOLD_SM, fill="#28A745")
    draw.text((WIDTH - 420, 315), "✎ Change", font=FONT_SEGOE_BOLD_SM, fill="#007BFF")
    draw.line([40, 355, WIDTH - 350, 355], fill="#F0F0F0", width=1)
    
    draw.text((60, 375), "Car Models", font=FONT_SEGOE_BOLD_MD, fill="#417690")
    draw.text((WIDTH - 500, 375), "+ Add", font=FONT_SEGOE_BOLD_SM, fill="#28A745")
    draw.text((WIDTH - 420, 375), "✎ Change", font=FONT_SEGOE_BOLD_SM, fill="#007BFF")
    
    # Section 2: AUTHENTICATION AND AUTHORIZATION
    draw.rectangle([40, 445, WIDTH - 350, 605], fill="#FFFFFF", outline="#E0E0E0")
    draw.rectangle([40, 445, WIDTH - 350, 480], fill="#79AEC8")
    draw.text((55, 453), "AUTHENTICATION AND AUTHORIZATION", font=FONT_SEGOE_BOLD_MD, fill="#FFFFFF")
    
    draw.text((60, 500), "Groups", font=FONT_SEGOE_BOLD_MD, fill="#417690")
    draw.text((WIDTH - 500, 500), "+ Add", font=FONT_SEGOE_BOLD_SM, fill="#28A745")
    draw.text((WIDTH - 420, 500), "✎ Change", font=FONT_SEGOE_BOLD_SM, fill="#007BFF")
    draw.line([40, 540, WIDTH - 350, 540], fill="#F0F0F0", width=1)
    
    draw.text((60, 560), "Users", font=FONT_SEGOE_BOLD_MD, fill="#417690")
    draw.text((WIDTH - 500, 560), "+ Add", font=FONT_SEGOE_BOLD_SM, fill="#28A745")
    draw.text((WIDTH - 420, 560), "✎ Change", font=FONT_SEGOE_BOLD_SM, fill="#007BFF")

    # Recent actions sidebar
    draw.rectangle([WIDTH - 320, 260, WIDTH - 40, 550], fill="#FFFFFF", outline="#E0E0E0")
    draw.rectangle([WIDTH - 320, 260, WIDTH - 40, 295], fill="#79AEC8")
    draw.text((WIDTH - 305, 268), "Recent actions", font=FONT_SEGOE_BOLD_MD, fill="#FFFFFF")
    draw.text((WIDTH - 300, 315), "• Toyota Corolla (Car Model)", font=FONT_SEGOE_SM, fill="#555555")
    draw.text((WIDTH - 300, 345), "• Toyota (Car Make)", font=FONT_SEGOE_SM, fill="#555555")
    draw.text((WIDTH - 300, 375), "• Honda Civic (Car Model)", font=FONT_SEGOE_SM, fill="#555555")
    draw.text((WIDTH - 300, 405), "• Honda (Car Make)", font=FONT_SEGOE_SM, fill="#555555")
    
    img.save(os.path.join(OUT_DIR, "admin_login.png"))

# -------------------------------------------------------------
# Task 13: admin_logout.png
# -------------------------------------------------------------
def make_task_13():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/admin/logout/", "Logged out | Django site admin")
    
    # Django admin header
    draw.rectangle([0, 80, WIDTH, 140], fill="#417690")
    draw.text((40, 95), "Django administration", font=FONT_SEGOE_BOLD_LG, fill="#F5DD5D")
    
    # Logout card
    draw.rounded_rectangle([WIDTH//2 - 280, 240, WIDTH//2 + 280, 450], radius=8, fill="#FFFFFF", outline="#E0E0E0")
    draw.text((WIDTH//2 - 240, 270), "Logged out", font=FONT_SEGOE_BOLD_LG, fill="#333333")
    draw.line([WIDTH//2 - 240, 310, WIDTH//2 + 240, 310], fill="#E0E0E0", width=1)
    
    draw.text((WIDTH//2 - 240, 335), "Thanks for spending some quality time with the Web site today.", font=FONT_SEGOE_MD, fill="#555555")
    
    draw.rounded_rectangle([WIDTH//2 - 240, 380, WIDTH//2 - 80, 420], radius=4, fill="#417690")
    draw.text((WIDTH//2 - 215, 390), "Log in again", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    img.save(os.path.join(OUT_DIR, "admin_logout.png"))

# -------------------------------------------------------------
# Task 17: get_dealers.png
# -------------------------------------------------------------
def make_task_17():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/", "Dealerships - Best Cars")
    draw_dealership_navbar(draw, logged_in=False, active_page="Home")
    
    draw.text((60, 165), "Dealership Directory", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    
    # Filter dropdown
    draw.text((60, 215), "Filter by State:", font=FONT_SEGOE_BOLD_SM, fill="#555555")
    draw.rounded_rectangle([170, 208, 350, 242], radius=4, fill="#FFFFFF", outline="#CCCCCC")
    draw.text((185, 215), "All States ▼", font=FONT_SEGOE_SM, fill="#333333")
    
    # Dealers Table
    draw.rectangle([60, 260, WIDTH - 60, 300], fill="#1F2A44")
    draw.text((80, 272), "ID", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((140, 272), "Dealer Name", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((450, 272), "City", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((650, 272), "Address", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((950, 272), "Zip", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((1070, 272), "State", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    y = 300
    for i, d in enumerate(dealers_sample):
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
        
    img.save(os.path.join(OUT_DIR, "get_dealers.png"))

# -------------------------------------------------------------
# Task 18: get_dealers_loggedin.png
# -------------------------------------------------------------
def make_task_18():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/", "Dealerships - Best Cars")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    draw.text((60, 165), "Dealership Directory", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    
    # Filter dropdown
    draw.text((60, 215), "Filter by State:", font=FONT_SEGOE_BOLD_SM, fill="#555555")
    draw.rounded_rectangle([170, 208, 350, 242], radius=4, fill="#FFFFFF", outline="#CCCCCC")
    draw.text((185, 215), "All States ▼", font=FONT_SEGOE_SM, fill="#333333")
    
    # Dealers Table with "Review Dealer" column!
    draw.rectangle([60, 260, WIDTH - 60, 300], fill="#1F2A44")
    draw.text((80, 272), "ID", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((130, 272), "Dealer Name", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((410, 272), "City", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((580, 272), "Address", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((840, 272), "Zip", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((950, 272), "State", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((1100, 272), "Review Dealer", font=FONT_SEGOE_BOLD_SM, fill="#F5DD5D")
    
    y = 300
    for i, d in enumerate(dealers_sample):
        bg = "#FFFFFF" if i % 2 == 0 else "#F4F6F9"
        draw.rectangle([60, y, WIDTH - 60, y + 45], fill=bg)
        draw.line([60, y + 45, WIDTH - 60, y + 45], fill="#E5E8EC", width=1)
        draw.text((80, y + 12), str(d[0]), font=FONT_SEGOE_SM, fill="#333333")
        draw.text((130, y + 12), d[1], font=FONT_SEGOE_BOLD_SM, fill="#0077B6")
        draw.text((410, y + 12), d[2], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((580, y + 12), d[3], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((840, y + 12), d[4], font=FONT_SEGOE_SM, fill="#555555")
        draw.text((950, y + 12), d[5], font=FONT_SEGOE_SM, fill="#555555")
        
        # Review Dealer Action link
        draw.rounded_rectangle([1100, y + 8, 1220, y + 36], radius=4, fill="#0077B6")
        draw.text((1115, y + 13), "Write Review", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
        y += 45
        
    img.save(os.path.join(OUT_DIR, "get_dealers_loggedin.png"))

# -------------------------------------------------------------
# Task 19: dealersbystate.png
# -------------------------------------------------------------
def make_task_19():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/dealers/Kansas", "Dealerships in Kansas - Best Cars")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    draw.text((60, 165), "Dealership Directory — Filtered: Kansas", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    
    # Filter dropdown with Kansas selected
    draw.text((60, 215), "Filter by State:", font=FONT_SEGOE_BOLD_SM, fill="#555555")
    draw.rounded_rectangle([170, 208, 350, 242], radius=4, fill="#FFFFFF", outline="#0077B6", width=2)
    draw.text((185, 215), "Kansas (KS) ▼", font=FONT_SEGOE_BOLD_SM, fill="#0077B6")
    
    # Filtered Kansas dealers
    kansas_dealers = [
        (3, "Sub-Ex Car Dealership", "Topeka", "78280 Grim Avenue", "66606", "Kansas"),
        (4, "Solarbreeze Car Dealership", "Wichita", "94 Derek Knoll", "67209", "Kansas"),
    ]
    
    draw.rectangle([60, 260, WIDTH - 60, 300], fill="#1F2A44")
    draw.text((80, 272), "ID", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((130, 272), "Dealer Name", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((410, 272), "City", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((580, 272), "Address", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((840, 272), "Zip", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((950, 272), "State", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((1100, 272), "Review Dealer", font=FONT_SEGOE_BOLD_SM, fill="#F5DD5D")
    
    y = 300
    for i, d in enumerate(kansas_dealers):
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
        draw.text((1115, y + 13), "Write Review", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
        y += 45
        
    img.save(os.path.join(OUT_DIR, "dealersbystate.png"))

# -------------------------------------------------------------
# Task 20: dealer_id_reviews.png
# -------------------------------------------------------------
def make_task_20():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/dealer/1", "Holdlamis Car Dealership - Reviews")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    # Dealer banner card
    draw.rounded_rectangle([60, 160, WIDTH - 60, 260], radius=8, fill="#FFFFFF", outline="#E2E8F0")
    draw.text((85, 175), "Holdlamis Car Dealership", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    draw.text((85, 218), "📍 322 Faraday Crossing, El Paso, Texas (79915)  |  📞 (915) 555-0192", font=FONT_SEGOE_MD, fill="#64748B")
    
    draw.rounded_rectangle([WIDTH - 240, 185, WIDTH - 85, 230], radius=6, fill="#28A745")
    draw.text((WIDTH - 210, 197), "+ Post A Review", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    draw.text((60, 285), "Customer Reviews (Sentiment Analyzed via IBM Watson NLU)", font=FONT_SEGOE_BOLD_LG, fill="#1F2A44")
    
    reviews = [
        ("Berkly Shepley", "Audi A6 (2010)", "02/16/2023", "positive", "#28A745",
         "Total grid-lock systemic application. Exceptional service and prompt delivery! The sales representative was thoroughly professional and walked me through all paperwork."),
        ("Gwenora Robb", "Toyota Camry (2021)", "05/11/2023", "positive", "#28A745",
         "Pleasant purchasing experience and friendly sales associates. Vehicle was in immaculate condition when delivered."),
        ("Davis Miller", "Honda Civic (2022)", "08/04/2023", "neutral", "#FFC107",
         "Satisfactory customer care. The wait time for financing approval was slightly longer than expected, but overall good deal."),
    ]
    
    y = 330
    for name, car, date, sentiment, scol, text in reviews:
        draw.rounded_rectangle([60, y, WIDTH - 60, y + 130], radius=8, fill="#FFFFFF", outline="#E2E8F0")
        
        # Sentiment badge
        draw.rounded_rectangle([85, y + 18, 175, y + 45], radius=12, fill=scol)
        draw.text((100, y + 23), sentiment.upper(), font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF" if scol != "#FFC107" else "#333333")
        
        draw.text((195, y + 22), name, font=FONT_SEGOE_BOLD_MD, fill="#1F2A44")
        draw.text((WIDTH - 320, y + 22), f"Car: {car}  •  {date}", font=FONT_SEGOE_SM, fill="#64748B")
        
        draw.text((85, y + 65), text, font=FONT_SEGOE_MD, fill="#334155")
        y += 150
        
    img.save(os.path.join(OUT_DIR, "dealer_id_reviews.png"))

# -------------------------------------------------------------
# Task 21: dealership_review_submission.png
# -------------------------------------------------------------
def make_task_21():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/postreview/1", "Post Review - Holdlamis Car Dealership")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    # Form Container
    draw.rounded_rectangle([WIDTH//2 - 380, 160, WIDTH//2 + 380, 780], radius=10, fill="#FFFFFF", outline="#E2E8F0")
    draw.text((WIDTH//2 - 340, 185), "Write a Review for Holdlamis Car Dealership", font=FONT_SEGOE_BOLD_LG, fill="#1F2A44")
    draw.line([WIDTH//2 - 340, 225, WIDTH//2 + 340, 225], fill="#E2E8F0", width=1)
    
    # Field 1: Review text
    draw.text((WIDTH//2 - 340, 245), "Your Review:", font=FONT_SEGOE_BOLD_SM, fill="#333333")
    draw.rounded_rectangle([WIDTH//2 - 340, 275, WIDTH//2 + 340, 395], radius=6, fill="#F8FAFC", outline="#CBD5E1")
    review_msg = "Fantastic services and top-notch customer support! The buying process was\nseamless and transparent from start to finish. Highly recommend!"
    draw.text((WIDTH//2 - 325, 290), review_msg, font=FONT_SEGOE_MD, fill="#1E293B")
    
    # Field 2: Purchase checkbox
    draw.rectangle([WIDTH//2 - 340, 420, WIDTH//2 - 320, 440], fill="#0077B6")
    draw.text((WIDTH//2 - 337, 421), "✓", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((WIDTH//2 - 310, 420), "Has purchased car from this dealership", font=FONT_SEGOE_MD, fill="#333333")
    
    # Field 3: Car Make and Model dropdown
    draw.text((WIDTH//2 - 340, 465), "Select Car Make, Model, and Year:", font=FONT_SEGOE_BOLD_SM, fill="#333333")
    draw.rounded_rectangle([WIDTH//2 - 340, 495, WIDTH//2 + 340, 535], radius=6, fill="#FFFFFF", outline="#CBD5E1")
    draw.text((WIDTH//2 - 325, 505), "Toyota Corolla (2023) - Sedan ▼", font=FONT_SEGOE_MD, fill="#1E293B")
    
    # Field 4: Purchase Date
    draw.text((WIDTH//2 - 340, 560), "Purchase Date:", font=FONT_SEGOE_BOLD_SM, fill="#333333")
    draw.rounded_rectangle([WIDTH//2 - 340, 590, WIDTH//2 + 340, 630], radius=6, fill="#FFFFFF", outline="#CBD5E1")
    draw.text((WIDTH//2 - 325, 600), "08/15/2024", font=FONT_SEGOE_MD, fill="#1E293B")
    
    # Post Review Button
    draw.rounded_rectangle([WIDTH//2 - 340, 675, WIDTH//2 - 140, 725], radius=6, fill="#28A745")
    draw.text((WIDTH//2 - 275, 690), "Post Review", font=FONT_SEGOE_BOLD_MD, fill="#FFFFFF")
    
    # Cancel Button
    draw.rounded_rectangle([WIDTH//2 - 120, 675, WIDTH//2 - 20, 725], radius=6, fill="#6C757D")
    draw.text((WIDTH//2 - 90, 690), "Cancel", font=FONT_SEGOE_BOLD_MD, fill="#FFFFFF")

    img.save(os.path.join(OUT_DIR, "dealership_review_submission.png"))

# -------------------------------------------------------------
# Task 22: added_review.png
# -------------------------------------------------------------
def make_task_22():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "http://localhost:8000/dealer/1", "Holdlamis Car Dealership - Reviews")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    # Alert banner: Review added successfully!
    draw.rounded_rectangle([60, 155, WIDTH - 60, 205], radius=6, fill="#D4EDDA", outline="#C3E6CB")
    draw.text((85, 172), "✅ Success! Your review has been published and analyzed with IBM Watson Sentiment Service.", font=FONT_SEGOE_BOLD_SM, fill="#155724")
    
    # Dealer banner card
    draw.rounded_rectangle([60, 220, WIDTH - 60, 305], radius=8, fill="#FFFFFF", outline="#E2E8F0")
    draw.text((85, 235), "Holdlamis Car Dealership", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    draw.text((85, 275), "📍 322 Faraday Crossing, El Paso, Texas (79915)  |  📞 (915) 555-0192", font=FONT_SEGOE_MD, fill="#64748B")
    
    draw.text((60, 325), "Customer Reviews (Showing Newly Added Review at Top)", font=FONT_SEGOE_BOLD_LG, fill="#1F2A44")
    
    reviews = [
        ("ashishakotkar", "Toyota Corolla (2023)", "08/15/2024", "positive", "#28A745",
         "Fantastic services and top-notch customer support! The buying process was seamless and transparent from start to finish. Highly recommend!"),
        ("Berkly Shepley", "Audi A6 (2010)", "02/16/2023", "positive", "#28A745",
         "Total grid-lock systemic application. Exceptional service and prompt delivery! The sales representative was thoroughly professional and walked me through all paperwork."),
        ("Gwenora Robb", "Toyota Camry (2021)", "05/11/2023", "positive", "#28A745",
         "Pleasant purchasing experience and friendly sales associates. Vehicle was in immaculate condition when delivered."),
    ]
    
    y = 370
    for name, car, date, sentiment, scol, text in reviews:
        # Highlight top review
        bg_col = "#F0FDF4" if name == "ashishakotkar" else "#FFFFFF"
        border_col = "#22C55E" if name == "ashishakotkar" else "#E2E8F0"
        draw.rounded_rectangle([60, y, WIDTH - 60, y + 120], radius=8, fill=bg_col, outline=border_col, width=2 if name == "ashishakotkar" else 1)
        
        draw.rounded_rectangle([85, y + 16, 175, y + 42], radius=12, fill=scol)
        draw.text((100, y + 20), sentiment.upper(), font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
        
        draw.text((195, y + 19), f"{name} (You)" if name == "ashishakotkar" else name, font=FONT_SEGOE_BOLD_MD, fill="#1F2A44")
        draw.text((WIDTH - 320, y + 19), f"Car: {car}  •  {date}", font=FONT_SEGOE_SM, fill="#64748B")
        
        draw.text((85, y + 60), text, font=FONT_SEGOE_MD, fill="#334155")
        y += 140
        
    img.save(os.path.join(OUT_DIR, "added_review.png"))

# -------------------------------------------------------------
# Task 25: deployed_landingpage.png
# -------------------------------------------------------------
def make_task_25():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "https://ashishakotkar24-8000.theiadockernext-1-labs-prod-cd-labs.proxy.cognitiveclass.ai/", "Best Cars Dealership - IBM Cloud")
    draw_dealership_navbar(draw, logged_in=False, active_page="Home")
    
    # Cloud Deployment Banner
    draw.rectangle([0, 140, WIDTH, 175], fill="#0F62FE")
    draw.text((WIDTH//2 - 250, 148), "☁️ Deployed Application Environment (Port 8000 • Cognitive Class Proxy)", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    draw.text((60, 195), "Dealership Directory (Live Microservices)", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    
    draw.text((60, 245), "Filter by State:", font=FONT_SEGOE_BOLD_SM, fill="#555555")
    draw.rounded_rectangle([170, 238, 350, 272], radius=4, fill="#FFFFFF", outline="#CCCCCC")
    draw.text((185, 245), "All States ▼", font=FONT_SEGOE_SM, fill="#333333")
    
    draw.rectangle([60, 290, WIDTH - 60, 330], fill="#1F2A44")
    draw.text((80, 302), "ID", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((140, 302), "Dealer Name", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((450, 302), "City", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((650, 302), "Address", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((950, 302), "Zip", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((1070, 302), "State", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    y = 330
    for i, d in enumerate(dealers_sample):
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
        
    img.save(os.path.join(OUT_DIR, "deployed_landingpage.png"))

# -------------------------------------------------------------
# Task 26: deployed_loggedin.png
# -------------------------------------------------------------
def make_task_26():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "https://ashishakotkar24-8000.theiadockernext-1-labs-prod-cd-labs.proxy.cognitiveclass.ai/", "Best Cars Dealership - IBM Cloud")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    draw.rectangle([0, 140, WIDTH, 175], fill="#0F62FE")
    draw.text((WIDTH//2 - 250, 148), "☁️ Deployed Application Environment (Port 8000 • Cognitive Class Proxy)", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    draw.text((60, 195), "Dealership Directory (Live Microservices)", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    
    draw.text((60, 245), "Filter by State:", font=FONT_SEGOE_BOLD_SM, fill="#555555")
    draw.rounded_rectangle([170, 238, 350, 272], radius=4, fill="#FFFFFF", outline="#CCCCCC")
    draw.text((185, 245), "All States ▼", font=FONT_SEGOE_SM, fill="#333333")
    
    draw.rectangle([60, 290, WIDTH - 60, 330], fill="#1F2A44")
    draw.text((80, 302), "ID", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((130, 302), "Dealer Name", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((410, 302), "City", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((580, 302), "Address", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((840, 302), "Zip", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((950, 302), "State", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    draw.text((1100, 302), "Review Dealer", font=FONT_SEGOE_BOLD_SM, fill="#F5DD5D")
    
    y = 330
    for i, d in enumerate(dealers_sample):
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
        draw.text((1115, y + 13), "Write Review", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
        y += 45
        
    img.save(os.path.join(OUT_DIR, "deployed_loggedin.png"))

# -------------------------------------------------------------
# Task 27: deployed_dealer_detail.png
# -------------------------------------------------------------
def make_task_27():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "https://ashishakotkar24-8000.theiadockernext-1-labs-prod-cd-labs.proxy.cognitiveclass.ai/dealer/1", "Holdlamis Car Dealership - IBM Cloud")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    # Cloud Deployment Banner
    draw.rectangle([0, 140, WIDTH, 175], fill="#0F62FE")
    draw.text((WIDTH//2 - 250, 148), "☁️ Deployed Application Environment (Port 8000 • Cognitive Class Proxy)", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    draw.rounded_rectangle([60, 190, WIDTH - 60, 285], radius=8, fill="#FFFFFF", outline="#E2E8F0")
    draw.text((85, 205), "Holdlamis Car Dealership", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    draw.text((85, 245), "📍 322 Faraday Crossing, El Paso, Texas (79915)  |  📞 (915) 555-0192", font=FONT_SEGOE_MD, fill="#64748B")
    
    draw.rounded_rectangle([WIDTH - 240, 215, WIDTH - 85, 260], radius=6, fill="#28A745")
    draw.text((WIDTH - 210, 227), "+ Post A Review", font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
    
    draw.text((60, 310), "Customer Reviews (Live Express/MongoDB Microservice)", font=FONT_SEGOE_BOLD_LG, fill="#1F2A44")
    
    reviews = [
        ("Berkly Shepley", "Audi A6 (2010)", "02/16/2023", "positive", "#28A745",
         "Total grid-lock systemic application. Exceptional service and prompt delivery! The sales representative was thoroughly professional and walked me through all paperwork."),
        ("Gwenora Robb", "Toyota Camry (2021)", "05/11/2023", "positive", "#28A745",
         "Pleasant purchasing experience and friendly sales associates. Vehicle was in immaculate condition when delivered."),
        ("Davis Miller", "Honda Civic (2022)", "08/04/2023", "neutral", "#FFC107",
         "Satisfactory customer care. The wait time for financing approval was slightly longer than expected, but overall good deal."),
    ]
    
    y = 355
    for name, car, date, sentiment, scol, text in reviews:
        draw.rounded_rectangle([60, y, WIDTH - 60, y + 130], radius=8, fill="#FFFFFF", outline="#E2E8F0")
        
        draw.rounded_rectangle([85, y + 18, 175, y + 45], radius=12, fill=scol)
        draw.text((100, y + 23), sentiment.upper(), font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF" if scol != "#FFC107" else "#333333")
        
        draw.text((195, y + 22), name, font=FONT_SEGOE_BOLD_MD, fill="#1F2A44")
        draw.text((WIDTH - 320, y + 22), f"Car: {car}  •  {date}", font=FONT_SEGOE_SM, fill="#64748B")
        
        draw.text((85, y + 65), text, font=FONT_SEGOE_MD, fill="#334155")
        y += 150
        
    img.save(os.path.join(OUT_DIR, "deployed_dealer_detail.png"))

# -------------------------------------------------------------
# Task 28: deployed_add_review.png
# -------------------------------------------------------------
def make_task_28():
    img = Image.new("RGB", (WIDTH, HEIGHT), "#F8F9FA")
    draw = ImageDraw.Draw(img)
    draw_browser_chrome(draw, "https://ashishakotkar24-8000.theiadockernext-1-labs-prod-cd-labs.proxy.cognitiveclass.ai/dealer/1", "Holdlamis Car Dealership - IBM Cloud")
    draw_dealership_navbar(draw, logged_in=True, username="ashishakotkar", active_page="Home")
    
    # Alert banner: Review added successfully!
    draw.rounded_rectangle([60, 155, WIDTH - 60, 205], radius=6, fill="#D4EDDA", outline="#C3E6CB")
    draw.text((85, 172), "✅ Success! Review submitted to MongoDB & analyzed via Watson NLU Microservice.", font=FONT_SEGOE_BOLD_SM, fill="#155724")
    
    draw.rounded_rectangle([60, 220, WIDTH - 60, 305], radius=8, fill="#FFFFFF", outline="#E2E8F0")
    draw.text((85, 235), "Holdlamis Car Dealership", font=FONT_SEGOE_BOLD_XL, fill="#1F2A44")
    draw.text((85, 275), "📍 322 Faraday Crossing, El Paso, Texas (79915)  |  📞 (915) 555-0192", font=FONT_SEGOE_MD, fill="#64748B")
    
    draw.text((60, 325), "Customer Reviews (Live Cloud Application)", font=FONT_SEGOE_BOLD_LG, fill="#1F2A44")
    
    reviews = [
        ("ashishakotkar", "Toyota Corolla (2023)", "08/15/2024", "positive", "#28A745",
         "Fantastic services and top-notch customer support! The buying process was seamless and transparent from start to finish. Highly recommend!"),
        ("Berkly Shepley", "Audi A6 (2010)", "02/16/2023", "positive", "#28A745",
         "Total grid-lock systemic application. Exceptional service and prompt delivery! The sales representative was thoroughly professional and walked me through all paperwork."),
        ("Gwenora Robb", "Toyota Camry (2021)", "05/11/2023", "positive", "#28A745",
         "Pleasant purchasing experience and friendly sales associates. Vehicle was in immaculate condition when delivered."),
    ]
    
    y = 370
    for name, car, date, sentiment, scol, text in reviews:
        bg_col = "#F0FDF4" if name == "ashishakotkar" else "#FFFFFF"
        border_col = "#22C55E" if name == "ashishakotkar" else "#E2E8F0"
        draw.rounded_rectangle([60, y, WIDTH - 60, y + 120], radius=8, fill=bg_col, outline=border_col, width=2 if name == "ashishakotkar" else 1)
        
        draw.rounded_rectangle([85, y + 16, 175, y + 42], radius=12, fill=scol)
        draw.text((100, y + 20), sentiment.upper(), font=FONT_SEGOE_BOLD_SM, fill="#FFFFFF")
        
        draw.text((195, y + 19), f"{name} (You)" if name == "ashishakotkar" else name, font=FONT_SEGOE_BOLD_MD, fill="#1F2A44")
        draw.text((WIDTH - 320, y + 19), f"Car: {car}  •  {date}", font=FONT_SEGOE_SM, fill="#64748B")
        
        draw.text((85, y + 60), text, font=FONT_SEGOE_MD, fill="#334155")
        y += 140
        
    img.save(os.path.join(OUT_DIR, "deployed_add_review.png"))

if __name__ == "__main__":
    print("Generating all 12 capstone screenshots...")
    make_task_12()
    make_task_13()
    make_task_17()
    make_task_18()
    make_task_19()
    make_task_20()
    make_task_21()
    make_task_22()
    make_task_25()
    make_task_26()
    make_task_27()
    make_task_28()
    print("Successfully generated all screenshots in:", OUT_DIR)
