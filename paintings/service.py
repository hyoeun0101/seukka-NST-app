from paintings.models import Painting
from typing import List


def get_paints(offset: int, limit: int) -> List[Painting]:
    paints = Painting.objects.order_by("-created")[offset : offset + limit]
    print(paints)
    return paints
