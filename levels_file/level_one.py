map = (
    '002', '002', '002', '002', '002', '002', '002', '002', '002', '002',
    '002', '002', '002', '002', '999', '999', '002', '002', '002', '002',
    '002', '002', '003', '002', '002', '002', '007', '002', '003', '003',
    '002', '006', '002', '002', '002', '002', '002', '002', '017', '002',
    '002', '007', '002', '002', '004', '005', '002', '006', '002', '002',
    '002', '002', '002', '002', '014', '015', '016', '002', '013', '002',
    '002', '002', '017', '002', '002', '013', '002', '002', '002', '002',
    '002', '002', '002', '017', '002', '002', '002', '002', '016', '002',
    '002', '002', '006', '002', '002', '017', '002', '016', '003', '002',
    '002', '002', '002', '002', '002', '002', '002', '002', '002', '002',
)

collision = (
    '100', '101', '101', '101', '101', '101', '102', '102', '102', '103',
    '110', '111', '111', '111', '111', '111', '111', '111', '111', '112',
    '120', '000', '000', '000', '522', '522', '512', '000', '000', '121',
    '120', '000', '000', '000', '522', '522', '000', '000', '000', '121',
    '120', '000', '10' , '000', '000', '000', '000', '000', '000', '121',
    '120', '000', '000', '000', '000', '000', '000', '000', '000', '121',
    '120', '000', '11', '000', '000', '000', '000', '12', '000', '121',
    '120', '000', '000', '000', '000', '000' , '000', '000', '000', '121',
    '130', '131', '131', '131', '131', '131', '131', '131', '131', '132',
    '140', '141', '141', '141', '141', '141', '141', '141', '141', '142'
)

back_aesthetics = (
    '000', '000', '04', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '14', '000', '000', '000', '000', '000', '000', '000',
    '000', '3', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '022', '000', '000', '000',
    '000', '000', '000', '000', '4', '000', '000', '5'  , '000', '000',
    '000', '000', '000', '2', '000', '000', '023', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '033', '013', '000', '003', '000', '011', '000', '000', '000',
    '000', '000', '000', '000', '000', '1'  , '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
)

front_aesthetics = (
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '00', '000' , '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '01', '000', '000', '000', '000', '02', '000', '000',
    '000', '000', '000', '000', '000', '000' , '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
)

level_one_dict = {'map': map,
             'collidable': collision,
             'aestheticBack': back_aesthetics,
             'aestheticFront': front_aesthetics
             }
