
# وبسایت آموزش آنلاین

این یک وبسایت آموزش آنلاین است که منابع و دوره‌های آموزشی را برای کاربران ارائه می‌دهد. این وبسایت با استفاده از چارچوب پایتون Django ساخته شده است و از کتابخانه Pillow برای پردازش تصاویر، TinyMCE برای ویرایش متن پیشرفته و Allauth برای احراز هویت و ثبت نام کاربران استفاده می‌کند. این پروژه بر اساس یک قالب رایگان از [Colorlib](https://colorlib.com/wp/template/kiddos/) ساخته شده است که به‌طور سفارشی شده و گسترش یافته تا به نیازهای پلتفرم آموزش آنلاین پاسخ دهد.

![Math and English Institute](https://github.com/Abbas-Abbasi/Elearning/assets/137259478/c30d0f2b-4ae1-4be6-85f9-34435b08acf5)


## نصب
 
برای اجرای وبسایت به صورت محلی، مراحل زیر را دنبال کنید:

1. کلون کردن مخزن:

   ```
   git clone https://github.com/Abbas-Abbasi/Elearning.git
   ```

2. وارد شدن به دایرکتوری پروژه:

   ```
   cd Elearning
   ```

3. ایجاد محیط مجازی:

   ```
   python3 -m venv myenv
   ```

4. فعالسازی محیط مجازی:

   - برای macOS/Linux:

     ```
     source myenv/bin/activate
     ```

   - برای Windows:

     ```
     myenv\Scripts\activate
     ```

5. نصب وابستگی‌های مورد نیاز:

   ```
   pip install -r requirements.txt
   ```

6. اجرای مایگریشن‌های پایگاه داده:

   ```
   python manage.py migrate
   ```

7. راه‌اندازی سرور توسعه:

   ```
   python manage.py runserver
   ```

8. مرورگر خود را باز کرده و به آدرس [http://localhost:8000](http://localhost:8000) مراجعه کنید تا به وبسایت دسترسی پیدا کنید.

## استفاده

وبسایت آموزش آنلاین قابلیت‌های زیر را فراهم می‌کند:

- ص

فحه اصلی: معرفی پلتفرم و نمایش دوره‌ها و منابع آموزشی برجسته.
- کاتالوگ دوره‌ها: لیست دوره‌های موجود را نمایش می‌دهد و به کاربران امکان مرور و جستجوی موضوعات خاص را می‌دهد.
- جزئیات دوره: اطلاعات دقیق در مورد دوره‌ای خاص را ارائه می‌دهد، از جمله توضیحات دوره، جزئیات مربی و گزینه‌های ثبت‌نام.
- ثبت نام و احراز هویت کاربران: کاربران می‌توانند ثبت‌نام کنند، وارد شوند و حساب کاربری خود را مدیریت کنند. Allauth به عنوان یک افزونه استفاده شده است تا فرآیندهای احراز هویت و ثبت‌نام کاربران را در دست بگیرد.
- داشبورد مربی: این امکان را به مربیان ثبت‌شده می‌دهد که دوره‌های خود را ایجاد و مدیریت کنند، شامل افزودن محتوای دوره، آپلود تصاویر و به‌روزرسانی اطلاعات دوره.
- ویرایش متن پیشرفته: ویرایشگر TinyMCE به‌کار رفته است تا به مربیان امکان ایجاد محتوای دوره با تجربه ویرایش متن پیشرفته را بدهد.

## پیکربندی

تنظیمات پروژه Django در فایل `settings.py` قابل یافتن است. این فایل شامل تنظیمات مربوط به پایگاه داده، فایل‌های استاتیک، بارگذاری رسانه، احراز هویت و سایر تنظیمات مربوط به پروژه است. شما می‌توانید این فایل را براساس نیازهای خود تغییر دهید.

## همکاری

همکاری در این پروژه مورد استقبال قرار می‌گیرد. اگر می‌خواهید همکاری کنید، لطفا مراحل ز

یر را دنبال کنید:

1. فورک کردن مخزن در GitHub.
2. ایجاد یک شاخه جدید با نام توصیفی.
3. پیاده‌سازی تغییرات یا اضافه کردن ویژگی‌های جدید.
4. اعمال تغییرات خود با پیام‌های قابل فهم و کوتاه.
5. ارسال شاخه خود به مخزن فورک شده.
6. ارسال درخواست pull که تغییرات شما و مزایای آن را توضیح می‌دهد.

## مجوز

این پروژه تحت مجوز [مجوز MIT](LICENSE.md) ارائه می‌شود.

## قدردانی

- طراحی وبسایت بر اساس یک قالب رایگان از [Colorlib](https://colorlib.com/wp/template/kiddos/) است.
- تشکر ویژه از انجمن‌های Django، Pillow، TinyMCE و Allauth برای ارائه چارچوب‌ها و کتابخانه‌های برتری که به قابلیت‌ها و تجربه کاربری این وبسایت کمک می‌کنند.


-----------------------------------------------------------------------------------------------------------------
# Online Learning Website

This is an online learning website designed to provide educational resources and courses to users. The website is built using Python Django framework, with the integration of Pillow for image processing, TinyMCE for rich text editing, and Allauth for user authentication and registration. The project is based on a free template from [Colorlib](https://colorlib.com/wp/template/kiddos/), which has been customized and extended to meet the requirements of the online learning platform.

## Installation

To run the website locally, follow these steps:

1. Clone the repository:

   ```
   git clone https://github.com/Abbas-Abbasi/Elearning.git
   ```

2. Navigate to the project directory:

   ```
   cd Elearning
   ```

3. Create a virtual environment:

   ```
   python3 -m venv myenv
   ```

4. Activate the virtual environment:

   - For macOS/Linux:

     ```
     source myenv/bin/activate
     ```

   - For Windows:

     ```
     myenv\Scripts\activate
     ```

5. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```
   python manage.py migrate
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

8. Open your web browser and visit [http://localhost:8000](http://localhost:8000) to access the website.

## Usage

The online learning website provides the following features:

- Home Page: Introduces the platform and displays featured courses and resources.
- Course Catalog: Lists available courses, allowing users to browse and search for specific topics.
- Course Details: Provides detailed information about a specific course, including the course description, instructor details, and enrollment options.
- User Registration and Authentication: Users can register, log in, and manage their accounts. Allauth is integrated to handle user authentication and registration processes.
- Instructor Dashboard: Allows registered instructors to create and manage their courses, including adding course content, uploading images, and updating course information.
- Rich Text Editing: The TinyMCE editor is incorporated to enable instructors to create course content with a rich text editing experience.

## Configuration

The Django project configuration can be found in the `settings.py` file. This file contains settings related to database configuration, static files, media uploads, authentication, and other project-specific settings. You may modify this file as per your requirements.

## Contributing

Contributions to this project are welcome. If you would like to contribute, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch with a descriptive name.
3. Implement your changes or add new features.
4. Commit your changes with clear and concise commit messages.
5. Push your branch to your forked repository.
6. Submit a pull request, describing your changes and their benefits.

## License

This project is licensed under the [MIT License](LICENSE.md).

## Acknowledgments

- The website design is based on a free template from [Colorlib](https://colorlib.com/wp/template/kiddos/).
- Special thanks to the Django, Pillow, TinyMCE, and Allauth communities for providing excellent frameworks and libraries that contribute to the functionality and user experience of this website.
