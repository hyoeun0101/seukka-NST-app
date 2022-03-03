from typing import List

from paintings.models import Painting


def get_paints(offset: int, limit: int) -> List[Painting]:
    paints = Painting.objects.order_by("-created")[offset : offset + limit]
    print(paints)
    return paints
