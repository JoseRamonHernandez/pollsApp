from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def ramon(reques):
    return HttpResponse(
        """
            <nav>
                <h1>Polls APP</h1>
                <h3>Jose Ramon Hernandez Muñoz</h3>
            </nav>
        """
    )