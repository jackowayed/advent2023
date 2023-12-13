use itertools::iproduct;

fn print_grid(grid: &Vec<Vec<u8>>) {
    for row in grid {
        println!("{} ", String::from_utf8(row.to_vec()).unwrap());
    }
}

type Galaxy = (usize, usize);

fn axis_distance(p1: usize, p2: usize, empty_ranks: &Vec<usize>) -> usize {
    if p1 > p2 {
        return axis_distance(p2, p1, empty_ranks);
    }
    (p2 - p1) + empty_ranks.iter().filter(|r| **r > p1 && **r < p2).count() * 999999
}

fn main() {
    let grid: Vec<&[u8]> = 
    //include_str!("11.test")
        include_str!("11.in.txt")
        .lines()
        .map(|s| s.trim().as_bytes())
        .collect();
    let empty_rows = (0..grid.len())
        .filter(|y| grid[*y].iter().all(|c| *c == b'.'))
        .collect();
    let empty_cols = (0..grid[0].len())
        .filter(|x| (0..grid.len()).all(|y| grid[y][*x] == b'.'))
        .collect();
    let galaxies: Vec<Galaxy> = iproduct!(0..grid.len(), 0..grid[0].len())
        .filter(|(y, x)| grid[*y][*x] != b'.')
        .collect();

    // let distance = |g1: Galaxy, g2: Galaxy| -> usize {
    //     axis_distance(g1.0, g2.0, empty_rows) + axis_distance(g1.1, g2.1, empty_cols)
    // }
    let total_distance: usize = iproduct!(galaxies.clone(), galaxies.clone())
        .map(|(g1, g2)| {
            axis_distance(g1.0, g2.0, &empty_rows) + axis_distance(g1.1, g2.1, &empty_cols)
        })
        .sum::<usize>()
        / 2;
    println!("{:?}", total_distance);
}
