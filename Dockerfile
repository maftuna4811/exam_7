# Python imidjini tanlaymiz
FROM python:3.12

# Ishchi katalogni yaratamiz
WORKDIR /app

# Talablar faylini nusxalaymiz
COPY requirements.txt /app/

# Python kutubxonalarni o'rnatamiz
RUN pip install --no-cache-dir -r requirements.txt


# Butun loyihani nusxalaymiz
COPY . /app/

# Migratsiyalarni ishga tushiramiz
#RUN python manage.py migrate

# Django serverini ishga tushirish uchun buyruq
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]