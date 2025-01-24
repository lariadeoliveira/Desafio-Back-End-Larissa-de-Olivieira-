from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Usuario, Transferencia
from .serializers import UsuarioSerializer, TransferenciaSerializer

class UsuarioCreateView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuarioLoginView(TokenObtainPairView):
    # Customização do TokenObtainPairView pode ser feita aqui, se necessário
    pass

class TransferenciaCreateView(generics.CreateAPIView):
    queryset = Transferencia.objects.all()
    serializer_class = TransferenciaSerializer
    permission_classes = [IsAuthenticated]

class TransferenciaListView(generics.ListAPIView):
    serializer_class = TransferenciaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Transferencia.objects.filter(remetente=user)  # Filtra transferências do usuário logado

class SaldoView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        usuario = request.user
        saldo = usuario.carteira.saldo  # Supondo que o modelo de usuário tenha uma relação com carteira
        return Response({'saldo': saldo})