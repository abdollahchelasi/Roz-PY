import streamlit as st
import sqlite3
import streamlit.components.v1 as components
from datetime import datetime
from streamlit_option_menu import option_menu


st.set_page_config(
        page_title="جواهری رز",
        page_icon="logo.png",
        initial_sidebar_state='collapsed',
        layout='wide',
    )


con=sqlite3.connect('picscols.db')
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS pics(id TEXT, img BLOB, note TEXT)')

with open("c.css") as f:
    st.markdown(f"<style> {f.read()} </style>", unsafe_allow_html=True)




selected = option_menu (
      menu_title=None,
      options=[ "بازی کن","چت آنلاین" ,"ورود ادمین", "خانه"],
      icons=["phone","","key","house" ],
      menu_icon="cast",
      default_index=3,
      orientation="horizontal",

      styles={
         "container": {"background-color": "#ffffff"},
         "icon" : {"color": "#000000"},
         "nav-link-selected": {"background-color": "#b77110"},
         "nav-link": {"color" : "#000000","font-size": "19px", "text-align": "center_y: 0.0", "margin":"0px", "--hover-color": "#d4bb4a"},

        }
    )





    

if selected == "خانه":

    tab1, tab2, tab3 = st.tabs(["خانه 🏠", "نمونه کارها 🖼️", "تماس با من 📞"])

    with tab1:

        
        with st.expander("جواهری رز", expanded=True):

            st.video("roz.mp4",autoplay=True)
            st.image("logo.png",width=100)
            st.write("""
به دنیای :blue[جواهری رز] خوش آمدید! جایی که هنر و زیبایی در هم می‌آمیزند و هر قطعه جواهر، داستانی از ظرافت و اصالت را روایت می‌کند. ما در :blue[جواهری رز]، 
                     با افتخار طیف گسترده‌ای از زیورآلات طلا و جواهر را به شما ارائه می‌دهیم که پاسخگوی سلیقه‌های مختلف شماست.
:red[انگشترها تنها یک زیور نیستند] ، بلکه نمادی از شخصیت و سبک زندگی شما هستند. از انگشترهای ظریف و میناکاری شده گرفته تا انگشترهای نگین‌دار با طراحی‌های کلاسیک و مدرن، ما مجموعه‌ای متنوع از انگشترها را داریم که برای هر مناسبتی مناسب است.
:red[انگشترهای نامزدی و ازدواج: ]  نمادی از عشق و تعهد، با طراحی‌های خاص و نگین‌های درخشان.
انگشترهای روزمره: برای استفاده روزانه با طراحی‌های ساده و شیک.
:red[انگشترهای مجلسی :]  با طراحی‌های خاص و نگین‌های بزرگ برای مناسبت‌های ویژه. 
                     دستبندها زیبایی مچ دست شما را دوچندان می‌کنند و به استایل شما جلوه‌ای خاص می‌بخشند. از دستبندهای ظریف و زنجیری گرفته تا دستبندهای پهن و نگین‌دار، ما انواع دستبندها را با طرح‌ها و رنگ‌های متنوع ارائه می‌دهیم.

:red[دستبندهای طلا:] با عیارهای مختلف و طراحی‌های متنوع برای هر سلیقه‌ای.
:red[دستبندهای نقره:] با روکش طلا یا سنگ‌های تزئینی برای کسانی که به دنبال گزینه‌های اقتصادی‌تر هستند.
دستبندهای چرم: ترکیبی از چرم طبیعی و فلزات گران‌بها برای یک استایل خاص.
                     گردنبندها یکی از محبوب‌ترین زیورآلات هستند که به گردن شما جلوه‌ای زیبا می‌بخشند. از گردنبندهای ظریف و زنجیری گرفته تا گردنبندهای آویزدار با طرح‌های متنوع، ما مجموعه‌ای کامل از گردنبندها را داریم.

:red[گردنبندهای طلا:] با طرح‌های کلاسیک و مدرن و نگین‌های متنوع.
:red[گردنبندهای نقره:] با روکش طلا یا سنگ‌های تزئینی برای استفاده روزانه.
:red[گردنبندهای پلاک‌دار:] با پلاک‌های اسم، تاریخ تولد یا هر طرح دلخواه دیگری.
                     با بندها یکی از زیورآلات محبوب هستند که به مچ پا جلوه‌ای زیبا می‌بخشند. با بندهای طلا و نقره با طرح‌های متنوع و سنگ‌های تزئینی، ما مجموعه‌ای کامل از با بندها را داریم.

چرا :blue[جواهری رز] را انتخاب کنیم؟

کیفیت برتر: تمامی محصولات ما از بهترین مواد اولیه و با بالاترین استانداردهای کیفیت ساخته شده‌اند.
تنوع بالا: طیف گسترده‌ای از زیورآلات با طرح‌ها و قیمت‌های متنوع.
طراحی‌های منحصر به فرد: بسیاری از محصولات ما دارای طراحی‌های منحصر به فرد و دست‌ساز هستند.
""")
     

            

    #         annotated_text(
    #     "خدمات ",
    #     ("دکوراسیون", "نصب PVC"),
    #     " و ",
    #     ("نصب کناف", "نصب ترمووال"),
    #     "نصب قرنیز",
    #     ("و نصب ماربل شیت", "با طرح های مختلف"),
    #     ("در", "سر تا سر"),
    #     " جزیره قشم ",
    #     ("با مدیریت","عبدالباسط زیوری"),
    #     ("شماره تماس :","09173663866"),
        
    # )
        


            st.divider()    
        for row in cur.execute('SELECT rowid, id, img, note FROM pics ORDER BY id'):
        # with st.form(f'ID-{row[0]}', clear_on_submit=True):
            st.write("---")
            imgcol, notecol = st.columns([3, 2])
        # id=notecol.text_input('id', row[1])
            id=notecol.text_input('کد محصول', row[1])
            note=notecol.text_area('اسم محصول', row[3])

            
            if row[2]:
                img=row[2]
                imgcol.image(row[2])
                






















    with tab2:

        c1 ,c2,c3 = st.columns(3)

        with c1:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g1.jpg")

                st.success("گردنبند ظریف دو ردیفه")
                st.error("وزن: 3/50 گرم")




        with c2:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g2.jpg")

                st.success("گردنبند و انگشتر نیم ست خوشگل البرنادو")
                st.error("وزن: نیم ست با زنجیر 14/50 گرم")
                st.warning("وزن: نیم ست بدون زنجیر 12/75 گرم")



        with c3:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g3.jpg")

                st.success("گردنبند ظریف دوتکه‌ی بی نهایت")
                st.error("وزن: 3.5گرم")



        with c1:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g4.jpg")
                st.success("گردنبند نیم ست خوشگل و جذاب گل رُز")
                st.error("وزن کل نیم ست بازنجیر : 4/70گرم")

            



        with c2:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g5.jpg")

                st.success("سرویس زیبا و جذاب کارتیر خوش تراش")
                st.error("وزن کل سرویس: 16/70 گرم")



        with c3:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g7.jpg")

                st.success("نیم ست ظریف‌‌ و پرطرفدار طرح LV")
                st.error("وزن کل ست: 9/150 گرم")






        with c1:

            
            with st.expander("جواهری رز", expanded=True):
                st.image("g8.jpg")

                st.success("نیم ست گوی نگین دار دستبند , گوشواره و گردنبند")
                st.error("وزن نیمست: 3/90 گرم")




        with c2:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g9.jpg")

                st.success("سرویس زیبای سکه ای ریز")
                st.error("وزن کل سرویس: 18 گرم")



        with c3:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g10.jpg")

                st.success("گوشواره فانتزی هندسی")
                st.error("""
وزن گوشواره بالا سمت چپ : 3.55 گرم

وزن گوشواره بالا سمت راست : 2.90 گرم

وزن گوشواره پایین سمت چپ : 2.85 گرم

وزن گوشواره پایین سمت راست : 2.85
""")




        with c1:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g11.jpg")

                st.success("گوشواره بچه‌گانه")
                st.error("وزن:بین 1 تا 2 گرم")




        with c2:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g12.jpg")

                st.success("مدل‌ها‌ی‌ جدید پابند")
                st.error("وزن: بین 1.5 تا 2.5 گرم")



        with c3:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g13.jpg")

                st.success("انگشتر طرح کویتی")
                st.error("وزن:بین 4 تا 6 گرم")




        with c2:

    
            with st.expander("جواهری رز", expanded=True):
                st.image("g14.jpg")

                st.success("دستبند های سبک جدید کارتیر")
                st.error("وزن: حدود 6.5 گرم")




    with tab3:
        st.divider()
    
        st.subheader("با مدیریت خلیل شادمان")
        st.divider()
    
      # st.markdown(f'<a href="tel:{phone_number}">{phone_number}</a>', unsafe_allow_html=True)
        st.markdown("[شمار ه تماس](tel:989170220100)")
      

        st.subheader("""
آدرس : جزیره قشم - شهر درگهان , خیابان‌ رسول‌اکرم‌ بازار ‌طلافروشی‌ پاساژ طلا و جواهرات‌ الماس


""")






elif selected == "ورود ادمین":
        username = st.text_input(label="نام کاربری", placeholder="Username")
        password = st.text_input(label="پسورد", placeholder="password", type="password")
        b = st.button("ورود")

        if username == "a" and password == "z":

            st.success("خوش آمدید برادرم , عبدالباسط")

            st.success(
            "توجه : لطفا با اضافه کردن محصول محصولات خود رو کامل پر کنید (عکس محصول , کد محصول , نام محصول) این ها نباید خالی باشد"
        )
            st.error(
            "هشدار : کد و نام محصولات شما نباید مثل محصولات دیگه ای که اضافه میکنید باشد. کد محصولات رو با اعداد انگلیسی و از شماره بالا به پایین شروع کنید . مانند : ( از 999 شروع کنید به پایین) "
        )

            if st.button("اضافه کردن محصول"):
                cur.execute("INSERT INTO pics(id, img, note) VALUES(?,?,?)", ("", "", ""))
                con.commit()

                st.write("---")

            for row in cur.execute("SELECT rowid, id, img, note FROM pics ORDER BY id"):
                with st.form(f"ID-{row[0]}", clear_on_submit=True):

                    imgcol, notecol = st.columns([3, 2])
                    id = notecol.text_input("کد محصول", row[1])
                    note = notecol.text_area("نام محصول", row[3])
                    if row[2]:
                    
                        img = row[2]
                        imgcol.image(row[2])
                    file = imgcol.file_uploader("تصاویر", ["png", "jpg", "gif", "jpeg", "bmp"])
                    if file:
                        img = file.read()
                    if notecol.form_submit_button("ذخیره محصول"):
                    
                        cur.execute(
                        "UPDATE pics SET id=?, img=?, note=? WHERE id=?;",
                        (id, img, note, str(row[1])),
                    )

                        con.commit()
                        st.rerun()


                    if notecol.form_submit_button("حذف محصول"):
                        cur.execute(f"""DELETE FROM pics WHERE rowid="{row[0]}";""")
                        con.commit()
                        st.rerun()

        elif username or password == "admin":
        
            st.error("لطفا درست وارد کنید")
    
    



elif selected == "بازی کن":
        
        st.write("بازی جوجه قشمی اینبار در برنامه :red[جواهری رز]")

        components.html("""

    <html><head><base href="https://websimgames.com/flappy-bird/" target="_blank"><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>بازی فلاپی پرنده</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            # background-color: #87CEEB;
            font-family: Arial, sans-serif;
        }
        #gameCanvas {
            border: 2px solid #fff;
            height: 210px;
        }
        #startScreen, #gameOverScreen {
            position: absolute;
            text-align: center;
            font-size: 14px;
            color: #fff;
            text-shadow: 2px 2px 4px #000;
            background-color: rgba(0,0,0,0.5);
            padding: 20px;
            border-radius: 10px;
        }
        #gameOverScreen {
            display: none;
        }
        button {
            font-size: 20px;
            padding: 10px 20px;
            margin-top: 10px;
            cursor: pointer;
        }
    </style>
    </head>
    <body>
    <canvas id="gameCanvas" width="288" height="312"></canvas>
    <div id="startScreen">
        <p>برای شروع بازی جوجه قشمی کلیک کنید</p>
    </div>
    <div id="gameOverScreen">
        <p>بازی تمام شد!</p>
        <p>امتیاز شما: <span id="finalScore"></span></p>
        <button id="restartButton">شروع مجدد</button>
    </div>

    <script>
    const canvas = document.getElementById('gameCanvas');
    const ctx = canvas.getContext('2d');
    const startScreen = document.getElementById('startScreen');
    const gameOverScreen = document.getElementById('gameOverScreen');
    const finalScoreElement = document.getElementById('finalScore');
    const restartButton = document.getElementById('restartButton');

    let bird = {
        x: 50,
        y: canvas.height / 2,
        velocity: 0,
        gravity: 0.5,
        lift: -7,
        size: 20
    };

    let pipes = [];
    let score = 0;
    let gameLoop;
    let gameStarted = false;

    // Load bird image
    const birdImg = new Image();
    birdImg.src = 'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MTIgNTEyIj48cGF0aCBmaWxsPSIjZmZkNzAwIiBkPSJNNDk2IDI1NmMwIDEzNi45LTExMS4xIDI0OC0yNDggMjQ4UzAgMzkyLjkgMCAyNTYgMTExLjEgOCAyNDggOHMyNDggMTExLjEgMjQ4IDI0OHoiLz48cGF0aCBmaWxsPSIjZmZhYTAwIiBkPSJNNDk2IDI1NmMwIDEzNi45LTExMS4xIDI0OC0yNDggMjQ4cy0yNDgtMTExLjEtMjQ4LTI0OEgzMTJsMTg0LTE4NHptLTI0OC0yNDh2MjQ4SDB6Ii8+PHBhdGggZmlsbD0iIzMzMyIgZD0iTTI0OCA1MmMtMTA4LjIgMC0xOTYgODcuOC0xOTYgMTk2czg3LjggMTk2IDE5NiAxOTYgMTk2LTg3LjggMTk2LTE5NlMzNTYuMiA1MiAyNDggNTJ6Ii8+PHBhdGggZmlsbD0iI2ZmZiIgZD0iTTMxMiAxOTJjMCAyNi41LTIxLjUgNDgtNDggNDhzLTQ4LTIxLjUtNDgtNDggMjEuNS00OCA0OC00OCA0OCAyMS41IDQ4IDQ4eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik00MTYgMjA4YzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0zODQgMjcyYzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjxwYXRoIGZpbGw9IiNmZmYiIGQ9Ik0zNTIgMzM2YzAgOC44LTcuMiAxNi0xNiAxNmgtMzJjLTguOCAwLTE2LTcuMi0xNi0xNnM3LjItMTYgMTYtMTZoMzJjOC44IDAgMTYgNy4yIDE2IDE2eiIvPjwvc3ZnPg==';

    function drawBird() {
        ctx.save();
        ctx.translate(bird.x, bird.y);
        ctx.rotate(bird.velocity * 0.1);
        ctx.drawImage(birdImg, -bird.size / 2, -bird.size / 2, bird.size, bird.size);
        ctx.restore();
    }

    function drawPipes() {
        pipes.forEach(pipe => {
            ctx.fillStyle = '#00AA00';
            ctx.fillRect(pipe.x, 0, pipe.width, pipe.top);
            ctx.fillRect(pipe.x, canvas.height - pipe.bottom, pipe.width, pipe.bottom);
        });
    }

    function drawScore() {
        ctx.fillStyle = '#FFF';
        ctx.font = '24px Arial';
        ctx.fillText(`امتیاز: ${score}`, 10, 30);
    }

    function updateGame() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        bird.velocity += bird.gravity;
        bird.y += bird.velocity;
        
        if (bird.y + bird.size / 2 > canvas.height) {
            gameOver();
        }
        
        if (pipes.length === 0 || pipes[pipes.length - 1].x < canvas.width - 200) {
            let gap = 150;
            let pipeHeight = Math.floor(Math.random() * (canvas.height - gap - 100)) + 50;
            pipes.push({
                x: canvas.width,
                top: pipeHeight,
                bottom: canvas.height - pipeHeight - gap,
                width: 50,
                counted: false
            });
        }
        
        pipes.forEach(pipe => {
            pipe.x -= 2;
            
            if (pipe.x + pipe.width < 0) {
                pipes.shift();
            }
            
            if (
                bird.x + bird.size / 2 > pipe.x &&
                bird.x - bird.size / 2 < pipe.x + pipe.width &&
                (bird.y - bird.size / 2 < pipe.top || bird.y + bird.size / 2 > canvas.height - pipe.bottom)
            ) {
                gameOver();
            }
            
            if (pipe.x + pipe.width < bird.x && !pipe.counted) {
                score++;
                pipe.counted = true;
            }
        });
        
        drawPipes();
        drawBird();
        drawScore();
        
        if (gameStarted) {
            gameLoop = requestAnimationFrame(updateGame);
        }
    }

    function gameOver() {
        cancelAnimationFrame(gameLoop);
        gameStarted = false;
        finalScoreElement.textContent = score;
        gameOverScreen.style.display = 'block';
    }

    function resetGame() {
        bird.y = canvas.height / 2;
        bird.velocity = 0;
        pipes = [];
        score = 0;
        gameOverScreen.style.display = 'none';
        gameStarted = true;
        gameLoop = requestAnimationFrame(updateGame);
    }

    canvas.addEventListener('click', () => {
        if (gameStarted) {
            bird.velocity = bird.lift;
        }
    });

    startScreen.addEventListener('click', () => {
        startScreen.style.display = 'none';
        resetGame();
    });

    restartButton.addEventListener('click', resetGame);

    // Initial draw
    drawBird();
    </script>
    </body></html>
    """,height=500)


        st.markdown("[دیجی کد ( آموزش ساخت بازی و برنامه )](https://myket.ir/app/abdollah.digicode)")










elif selected == "چت آنلاین":

        st.warning("توجه : برای مشاهده آخرین پیام ها به صفحه دیگری بروید و دوباره به همین صفحه بیایید .")

        with st.expander("چت با تیم جواهری رز", expanded=True):
        
        #   st.image('g2.png')
            st.subheader("🔻 چت آنلاین 🔻")
            
            conn = sqlite3.connect('chat.db')
            c = conn.cursor()

            # ایجاد جدول پیام‌ها اگر وجود نداشته باشد
            c.execute('''CREATE TABLE IF NOT EXISTS messages
                        (id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT,
                        message TEXT,
                        timestamp DATETIME)''')
            conn.commit()

            # تابع افزودن پیام جدید
            def add_message(username, message):
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                c.execute("INSERT INTO messages (username, message, timestamp) VALUES (?, ?, ?)",
                        (username, message, timestamp))
                conn.commit()

            # تابع دریافت تمام پیام‌ها
            def get_messages():
                c.execute("SELECT id, username, message, timestamp FROM messages ORDER BY timestamp DESC LIMIT 100")
                return c.fetchall()

            # تابع حذف پیام
            def delete_message(message_id):
                c.execute("DELETE FROM messages WHERE id = ?", (message_id,))
                conn.commit()

            # ورود نام کاربری
            
            
            username = st.text_input(": نام خود را وارد کنید")

            # نمایش پیام‌های موجود
            messages = get_messages()
            new_message = st.text_input(": پیام خود را وارد کنید")
            ersal = st.button("ارسال") 
            
            # ورودی پیام جدید
            if ersal and username and new_message :
            
                add_message(username, new_message)
                st.rerun()
            
            elif ersal and username and new_message == "":
                # add_message(username, new_message)
                st.error("لطفا پیام‌ خو بنویس" )

            elif ersal and new_message and username == "":
                # add_message(username, new_message)
                st.error("لطفا اسم خو بنویس")


            


            

            st.divider()

            for msg in messages:  # بدون معکوس کردن لیست پیام‌ها
                msg_id, msg_user, msg_text, msg_timestamp = msg
                st.success(f"{msg_timestamp} 🙋🏽‍♂️ {msg_user}: 💬 {msg_text}")
                
                # افزودن دکمه برای حذف پیام
                if st.button("حذف", key=f"delete_{msg_id}"):
                    delete_message(msg_id)
                    st.rerun()

            # بستن اتصال به پایگاه داده
            conn.close()






# if menu_id == "نمونه کار":

    







# if menu_id == "تماس با من":

    
          
    
      


  # with col2:
    # st.subheader("هتل ساحل طلایی قشم")





  # st.divider()















st.divider()
st.markdown("[طراحی شده توسط عبدالله چلاسی](sms:00989335825325)")



st.markdown("""
<style> 
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""",unsafe_allow_html=True)