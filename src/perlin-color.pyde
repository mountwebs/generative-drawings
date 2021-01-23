import datetime
w = 560
h = 500
inc = 0.2
scl = 8 # scale
cols = floor(w/scl+2)
rows = floor(h/scl+2)
zoff = 0

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
filename = 'perlin_field_lines_z'
record = True

def setup():
    size(w,h)
    

def draw():
    background(255)
    xoff = 0
    inc = 0.01
    global zoff

    for x in range(cols):
        yoff = 0
        for y in range(rows):
            r = noise(xoff,yoff,zoff)
            angle = r * TWO_PI
            v = PVector.fromAngle(angle)
            colorMode(HSB, 255)
            c = color(r * 255, 255,255)
            stroke(c)
            push()
            translate(x * scl, y *  scl)
            rotate(v.heading())
            #rect(x * scl,y*scl,scl,scl)
            line(0,0,scl,0)
            pop()
            yoff += inc
        xoff += inc
    zoff += 0.01
    #noLoop()
    if record:
        save_frame_timestamp(filename, timestamp)
        
counter = 0;

def save_frame_timestamp(filename, timestamp='', output_dir='output'):
    global counter
    counter += 1
    print(counter)
    '''Saves each frame with a structured filename to allow for tracking all output'''
    filename = filename.replace('\\', '')
    filename = filename.replace('/', '')
    output_filename = os.path.join(output_dir, '{}_{}_####.png'.format(timestamp, filename))
    
    saveFrame(output_filename)
