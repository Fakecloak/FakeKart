import os  

a=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(a)



#153 = 1*1*1 + 5*5*5 + 3*3*3

import math

a=str(153)

b=(math.pow(int(a[0]),len(a)) + pow(int(a[1]),len(a)) + pow(int(a[2]),len(a)))
print(b)
if (int(a)==int(b)):
    print("number is armstrong")
else:
    print("number is not armstrong")





{%load static%}
<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>
        {% block title %}
        {% endblock title %}
    </title>

        <!-- Bootstrap CSS and JS scripts -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js"></script>
        
        <!-- Css file-->
        <link rel="stylesheet" href="{% static 'css/style.css' %}">

        <!--font awesome file-->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

        <!-- JavaScript and jQuery -->
        <script src="//cdn.jsdelivr.net/npm/alertifyjs@1.13.1/build/alertify.min.js"></script>

        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>

        <!-- CSS -->
        <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/alertifyjs@1.13.1/build/css/alertify.min.css"/>



        

  </head>
  <body>

    {% include 'FakeKart/inc/navbar.html' %}
    
    {% block content %}
    {% endblock content %}

    {% block scripts %}
    {% endblock scripts %}


    <!-- Modal -->
<div class="modal fade" id="Mymessage" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="Mymessage">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body text-center">
        {% include 'FakeKart/inc/message.html' %}
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Understood</button>
      </div>
    </div>
  </div>
</div>











    {% include 'FakeKart/inc/footer.html' %}

  </body>
</html>