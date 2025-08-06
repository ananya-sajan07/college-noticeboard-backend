from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Notice
from .serializers import NoticeSerializer

@api_view(['GET'])
def get_notices(request):
    notices = Notice.objects.filter(is_active=True).order_by('-created_at')
    serializer = NoticeSerializer(notices, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_notice(request):
    serializer = NoticeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
