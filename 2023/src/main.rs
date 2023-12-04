mod day1;
mod day2;
mod utils;

fn main() {
    println!("Day 1");
    println!("\tPart 1: {}", day1::solution_pt1("day1/input.txt"));
    println!("\tPart 2: {}", day1::solution_pt2("day1/input.txt"));
    println!("\n==========\n");
    println!("Day 2");
    println!("\tPart 1: {}", day2::solution_pt1("day2/input.txt"));
}
