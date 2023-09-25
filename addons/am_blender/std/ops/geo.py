from ...std import *
from ...std import ops
from mathutils import Vector

class Geo:
    @staticmethod
    @log.catch
    def mesh_bounds(obj: 'Object') -> Union[Tuple[Vector, Vector], None]:
        """
        Compute the actual bounds of a mesh object using its vertices in object space (local coordinates).
        
        Parameters:
        - obj: The mesh object to compute bounds for.
        
        Returns:
        - (min_bound, max_bound): A tuple containing the minimum and maximum bounds as Vector objects.
        """
        
        # Ensure the object is a mesh
        if obj.type != 'MESH':
            log.error(f"Object {obj.name} is not a mesh.")
            return None

        # Extract all vertex positions as a list of vectors
        vertex_positions = [vertex.co for vertex in obj.data.vertices]

        # Calculate the min and max bounds using Python's built-in functions and list comprehensions
        min_bound = Vector((min(pos.x for pos in vertex_positions),
                            min(pos.y for pos in vertex_positions),
                            min(pos.z for pos in vertex_positions)))
        max_bound = Vector((max(pos.x for pos in vertex_positions),
                            max(pos.y for pos in vertex_positions),
                            max(pos.z for pos in vertex_positions)))

        return (min_bound, max_bound)

geo = Geo()
