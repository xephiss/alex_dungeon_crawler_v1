map = (
    '002', '002', '002', '002', '002', '002', '002', '002', '002', '002',
    '002', '002', '002', '002', '002', '002', '002', '002', '002', '002',
    '002', '016', '003', '017', '002', '002', '002', '003', '002', '012',
    '002', '002', '002', '002', '016', '017', '002', '002', '003', '002',
    '999', '002', '003', '004', '013', '013', '005', '002', '017', '002',
    '999', '003', '002', '014', '012', '006', '015', '002', '012', '002',
    '007', '002', '002', '002', '016', '017', '002', '002', '017', '002',
    '002', '012', '002', '002', '002', '002', '002', '003', '002', '002',
    '002', '002', '002', '003', '003', '002', '012', '002', '002', '002',
    '002', '002', '002', '002', '002', '002', '002', '002', '002', '002',
)

collision = (
    '100', '101', '101', '402', '403', '101', '408', '102', '102', '103',
    '110', '111', '111', '412', '413', '111', '418', '111', '111', '112',
    '120', '000', '000', '000', '000', '000', '000', '000', '000', '121',
    '120', '000', '000', '000', '000', '000', '10',  '000', '000', '121',
    '120',  '10', '000', '000', '000', '000', '000', '000', '000', '121',
    '120',  '11', '000', '000', '000', '000', '000',  '10', '000', '121',
    '120', '000', '000', '000', '000', '000', '000',  '12', '000', '121',
    '120', '000', '000',  '12', '000', '000', '000', '000', '000', '121',
    '130', '131', '131', '131', '131', '131', '131', '131', '131', '132',
    '140', '141', '141', '141', '141', '141', '141', '141', '141', '142'
)

back_aesthetics = (
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '001', '000', '000', '011', '000', '011', '000', '000', '000',
    '000', '000', '000',   '0',   '6',   '6', '000', '000', '000', '000',
    '000', '000', '022',   '6', '002', '033',   '6', '000', '000', '000',
    '000', '000', '000',   '6', '023', '031',   '6', '000', '000', '000',
    '000', '013', '000',   '2',   '6',   '6',   '4', '000', '013', '000',
    '000', '000', '000', '000',   '5', '000', '000', '000', '000', '000',
    '000', '031', '000', '003', '000', '000', '000', '000', '022', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
)

front_aesthetics = (
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000',  '00', '000', '000', '000',
    '000',  '00', '000', '000', '000', '000', '000', '000', '000', '000',
    '000',  '01', '000', '000', '000', '000', '000',  '00', '000', '000',
    '000', '000', '000', '000', '000', '000', '000',  '02', '000', '000',
    '000', '000', '000',  '02', '000', '000', '000', '000', '000', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
    '000', '131', '131', '131', '131', '000', '000', '000', '131', '000',
    '000', '000', '000', '000', '000', '000', '000', '000', '000', '000',
)

level_three_dict = {'map': map,
             'collidable': collision,
             'aestheticBack': back_aesthetics,
             'aestheticFront': front_aesthetics
             }