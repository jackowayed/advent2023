fn extrapolate_sequence(seq: &Vec<i64>) -> i64 {
    let mut sequences = vec![seq.to_vec()];
    while sequences.last().unwrap().iter().any(|i| *i != 0) {
        let cur_seq = sequences.last().unwrap();
        sequences.push(
            (1..cur_seq.len())
                .map(|i| cur_seq[i] - cur_seq[i - 1])
                .collect(),
        )
    }
    /*
    println!(
        "{:?}",
        sequences
            .iter()
            .map(|seq| *seq.last().unwrap())
            .collect::<Vec<i64>>()
    );
    */
    sequences.iter().map(|seq| seq.last().unwrap()).sum()
    // let extrapolated_vals: Vec<i64> = sequences
    //     .iter()
    //     .map(|s| 2 * s[s.len() - 1] - s[s.len() - 2])
    //     .collect();
    // //extrapolated_vals.iter().sum()
}

fn extrapolate_backwards(seq: &Vec<i64>) -> i64 {
    let mut sequences = vec![seq.to_vec()];
    while sequences.last().unwrap().iter().any(|i| *i != 0) {
        let cur_seq = sequences.last().unwrap();
        sequences.push(
            (1..cur_seq.len())
                .map(|i| cur_seq[i] - cur_seq[i - 1])
                .collect(),
        )
    }
    //sequences[0][0] * 2 - sequences.iter().map(|seq| seq.last().unwrap()).sum::<i64>()
    let mut extrapolations = vec![0i64];
    for s in sequences.iter().rev() {
        extrapolations.push(s[0] - extrapolations.last().unwrap());
    }
    *extrapolations.last().unwrap()
}
fn main() {
    let lines = include_str!("9.in.txt").lines();
    let sequences: Vec<Vec<i64>> = lines
        .map(|l| {
            l.split_whitespace()
                .map(|i| i.parse::<i64>().unwrap())
                .collect()
        })
        .collect();
    //let answer: Vec<i64> = sequences.iter().map(extrapolate_sequence).collect();
    let part_1_answer: i64 = sequences.iter().map(extrapolate_sequence).sum();
    println!("{:?}", part_1_answer);
    println!(
        "{:?}",
        sequences.iter().map(extrapolate_backwards).sum::<i64>()
    );
}
