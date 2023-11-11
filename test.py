bw = ["black", "white", "green"]




def segment_colour_selector():
    global colour_scheme
    select_segment_colour = colour_scheme[0]
    colour_scheme.append(colour_scheme[0])
    colour_scheme[1:]
    return select_segment_colour

bw = segment_colour_selector(bw)

print(bw)

bw = segment_colour_selector(bw)

print(bw)

