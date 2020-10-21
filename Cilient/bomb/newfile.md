folder เป็นชื่อวันที่ที่ทำงาน แล้ว zip ไฟล์ลงไป

view.py
  def doRegister(request):
    return render(request,"register.html")
urls.py
  path('register',views.doRegister),
