def collider(entity, target):
    return (
        (entity.position["x"] < target.position["x"] + target.dimension["w"]) and
        (entity.position["x"] + entity.dimension["w"] > target.position["x"]) and 
        (entity.position["y"] < target.position["y"] + target.dimension["h"]) and
        (entity.position["y"] + entity.dimension["h"] > target.position["y"])
    )

