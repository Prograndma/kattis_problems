import math


def first_method(num_beams, num_arcs, radius, beam1, arc1, beam2, arc2):
    beam_chunk = radius / num_arcs
    beam_dist = abs(arc1 - arc2) * beam_chunk
    little_radius = min(arc1, arc2) * beam_chunk

    amount_of_semi_circle = abs(beam1 - beam2) / num_beams

    return beam_dist + amount_of_semi_circle * math.pi * little_radius


def other_method(num_arcs, radius, arc1, arc2):
    beam_chunk = radius / num_arcs
    return arc1 * beam_chunk + arc2 * beam_chunk


inputs = input().split()

num_beams = int(inputs[0])
num_arcs = int(inputs[1])
radius = float(inputs[2])

inputs = input().split()

beam1 = int(inputs[0])
arc1 = int(inputs[1])
beam2 = int(inputs[2])
arc2 = int(inputs[3])

result = min(first_method(num_beams, num_arcs, radius, beam1, arc1, beam2, arc2),
             other_method(num_arcs, radius, arc1, arc2))
print(result)
