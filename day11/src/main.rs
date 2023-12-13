use itertools::iproduct;

fn print_grid(grid: &Vec<Vec<u8>>) {
    for row in grid {
        println!("{} ", String::from_utf8(row.to_vec()).unwrap());
    }
}

fn main() {
    let mut wip_grid: Vec<Vec<u8>> = Vec::new();
    for line in include_str!("11.in.txt")
        .lines()
        .map(|s| s.trim().as_bytes().to_vec())
    {
        if line.iter().all(|c| *c == b'.') {
            wip_grid.push(line.clone());
        }
        wip_grid.push(line);
    }
    let mut grid: Vec<Vec<u8>> = vec![Vec::new(); wip_grid.len()];
    for x in 0..wip_grid[0].len() {
        let times = if (0..wip_grid.len()).all(|y| wip_grid[y][x] == b'.') {
            2
        } else {
            1
        };
        for _ in 0..times {
            for y in 0..wip_grid.len() {
                grid[y].push(wip_grid[y][x]);
            }
        }
    }
    print_grid(&grid);
    //let mut galaxies: Vec<(usize, usize)> = Vec::new();
    let galaxies: Vec<(usize, usize)> = iproduct!(0..grid.len(), 0..grid[0].len())
        .filter(|(y, x)| grid[*y][*x] != b'.')
        .collect();
    let distance = iproduct!(galaxies.clone(), galaxies.clone())
        .map(|((y1, x1), (y2, x2))| (y2 as i32 - y1 as i32).abs() + (x2 as i32 - x1 as i32).abs())
        .sum::<i32>()
        / 2;
    println!("{:?}", distance);
}
