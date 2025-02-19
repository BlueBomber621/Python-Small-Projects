car_levels = [
    # Level 1
    [
        [10, "red", -60, 5],
        [12, "red", 60, 5],
    ],
    # Level 2
    [
        [10, "red", -60, 5],
        [12, "red", 30, 5],
        [9, "red", 0, 5],
    ],
    # Level 3 - More variety in speed and colors
    [
        [11, "blue", -120, 4],
        [13, "green", 90, 6],
        [9, "yellow", 0, 5],
        [10, "red", 120, 5],
    ],
    # Level 4 - Increased speed and more cars
    [
        [14, "blue", -180, 4],
        [15, "green", 150, 6],
        [12, "yellow", 30, 5],
        [11, "red", 0, 4],
        [13, "purple", 90, 5],
    ],
    # Level 5 - Faster cars, more density
    [
        [16, "blue", -200, 3],
        [14, "green", 180, 5],
        [13, "yellow", 60, 4],
        [12, "red", -30, 3],
        [15, "purple", 90, 4],
        [17, "orange", 120, 6],
    ],
    # Level 6 - Even faster with more challenging spawn times
    [
        [18, "blue", -240, 3],
        [15, "green", 200, 4],
        [14, "yellow", 80, 3],
        [13, "red", -50, 3],
        [16, "purple", 100, 3],
        [19, "orange", 140, 5],
        [20, "black", 180, 6],
    ],
    # Level 7 - Extreme difficulty, max speed & randomness
    [
        [20, "blue", -210, 2],
        [18, "green", 220, 3],
        [14, "yellow", -100, 3],
        [16, "red", -160, 2],
        [12, "red", 40, 6],
        [19, "purple", 130, 3],
        [21, "orange", 160, 4],
        [20, "black", -70, 2],
    ],
    # Level 8 - Zoomy starter
    [
        [16, "blue", -180, 5],
        [18, "green", 190, 3],
        [20, "gray", 110, 16], [21, "gray", 110, 18], [19, "gray", 110, 14], 
        [17, "yellow", -190, 3],
        [16, "red", -110, 2],
    ],
    # Level 9 - Zoomy Lanes (Groups of 3, Slight Variations)
    [
        [20, "gray", -200, 18], [21, "gray", -200, 16], [19, "gray", -200, 14],  
        [21, "gray", -100, 18], [22, "gray", -100, 17], [20, "gray", -100, 16],  
        [22, "gray", 0, 20],    [23, "gray", 0, 22],    [21, "gray", 0, 18],  
        [21, "gray", 100, 18],  [22, "gray", 100, 20],  [20, "gray", 100, 16],  
        [21, "gray", 200, 19],  [20, "gray", 200, 17],  [19, "gray", 200, 15],  
    ],
    # Level 10 - Zoomy Mix
    [
        [18, "gray", -140, 12], [19, "gray", -140, 14], [17, "gray", -140, 16],  
        [19, "gray", 140, 14], [20, "gray", 140, 16], [18, "gray", 140, 18],  
        [20, "gray", 50, 16],    [21, "gray", 50, 18],    [19, "gray", 50, 20],
        [13, "yellow", 120, 7],
        [10, "red", -70, 2],
        [15, "purple", -120, 6],
    ],
    # Level 11 - SPEEEED
    [
        [11, "orange", 80, 4],
        [18, "black", -50, 3],
        [36, "cyan", 10, 30],
    ],
    # Level 12 - SPEEEED PT 2
    [
        [17, "blue", -200, 3],
        [12, "red", 80, 1],
        [15, "black", -130, 9],
        [36, "cyan", 20, 30],
        [36, "cyan", -20, 32],
    ],
    # Level 13 - Super speedy stairway
    [
        [36, "cyan", 100, 40],
        [36, "cyan", 70, 44],
        [36, "cyan", 40, 48],
        [36, "cyan", 10, 52],
        [36, "cyan", -20, 56],
        [36, "cyan", -50, 60],
        [36, "cyan", -80, 64],
    ],
    # Level 14 - Weave
    [
        [12, "blue", -120, 2],
        [15, "red", -100, 3],
        [12, "blue", -80, 2],
        [15, "red", -60, 3],
        [12, "blue", -40, 2],
        [15, "red", -20, 3],
        [12, "blue", 0, 2],
        [15, "red", 20, 3],
        [12, "blue", 40, 2],
        [15, "red", 60, 3],
        [12, "blue", 80, 2],
        [15, "red", 100, 3],
    ],
    # Level 15 - Full Chaos (Random speeds & colors, Gray triples)
    [
        [14, "blue", -180, 3], [16, "red", 180, 4], [15, "green", -140, 5],
        [18, "gray", -100, 8], [19, "gray", -100, 10], [17, "gray", -100, 12],
        [20, "orange", -60, 3], [12, "yellow", 60, 6],
        [36, "cyan", 20, 30], [36, "cyan", -20, 34],
    ],
    # Level 16 - Spaced Out, But Deadly
    [
        [17, "gray", -200, 9], [18, "gray", -200, 11], [16, "gray", -200, 13],
        [12, "blue", -150, 4], [14, "red", 150, 6], [15, "green", -120, 5],
        [36, "cyan", 80, 40], [36, "cyan", 50, 42], [36, "cyan", -30, 48],
        [20, "purple", 0, 3], [15, "black", -50, 8],
    ],
    # Level 17 - The ones without delay
    [
        [14, "blue", -150, 4], [16, "red", 150, 5],  
        [19, "gray", -100, 9], [20, "gray", -100, 11], [18, "gray", -100, 13],  
        [12, "orange", 80, 3], [15, "green", -180, 4],  
        [36, "cyan", 10, 40], [18, "brown", 100, 0], [15, "brown", -30, 0],
    ],
    # Level 18 - Absolute Chaos Grid
    [
        [21, "gray", -200, 8], [22, "gray", -200, 10], [20, "gray", -200, 12],
        [19, "gray", -100, 9], [20, "gray", -100, 11], [18, "gray", -100, 13],
        [36, "cyan", -50, 50], [36, "cyan", 10, 54], [36, "cyan", 70, 60],
        [13, "red", -120, 4], [17, "blue", 120, 3], [12, "orange", 90, 5],
        [15, "purple", -30, 6], [14, "green", 60, 4],
    ],
    # Level 19 - The ones without delay pt 2
    [
        [22, "gray", -200, 7], [23, "gray", -200, 9], [21, "gray", -200, 11],  
        [20, "gray", -100, 8], [21, "gray", -100, 10], [19, "gray", -100, 12],  
        [36, "cyan", -50, 55], [36, "cyan", 30, 58],  
        [15, "red", -120, 4], [17, "blue", 120, 3], [12, "purple", 90, 5],
        [18, "brown", -70, 0], [19, "brown", -140, 0], [12, "brown", 170, 0],
    ],
    # Level 20 - The Ultimate Gauntlet
    [
        [22, "gray", -200, 7], [23, "gray", -200, 9], [21, "gray", -200, 11],
        [20, "gray", -100, 8], [21, "gray", -100, 10], [19, "gray", -100, 12],
        [36, "cyan", 0, 60], [36, "cyan", -40, 65], [36, "cyan", 80, 70],
        [16, "blue", -150, 3], [19, "red", 150, 5], [14, "orange", -110, 6],
        [13, "green", 90, 3], [18, "purple", -30, 5], [12, "brown", -130, 0],
        [15, "brown", 210, 0],
    ]
]