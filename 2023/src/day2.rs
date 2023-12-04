use crate::utils;

const RED_COUNT: i32 = 12;
const GREEN_COUNT: i32 = 13;
const BLUE_COUNT: i32 = 14;


pub fn solution_pt1(input: &str) -> usize {
    let mut sum_valid_games: usize = 0;

    let lines = utils::parse_file(input);
    for i in 0..lines.len() {
        if is_valid_game(&lines[i]) {
            sum_valid_games += i+1;
        }
    }
    sum_valid_games
}

// pub fn solution_pt2(input: &str) -> i32 {
//     0
// }

fn is_valid_game(line: &str) -> bool {
    let (max_red, max_green, max_blue) = get_maxs_in_game(line);

    max_red <= RED_COUNT && max_green <= GREEN_COUNT && max_blue <= BLUE_COUNT
}

fn get_maxs_in_game(line: &str) -> (i32,i32,i32) {
    let mut max_red = 0;
    let mut max_green = 0;
    let mut max_blue = 0;
    let handfuls = line.split(":").collect::<Vec<&str>>()[1].split(";");
    for handful in handfuls {
        let (red, green, blue) = parse_handful(handful);
        if red > max_red {
            max_red = red;
        }
        if green > max_green {
            max_green = green;
        }
        if blue > max_blue {
            max_blue = blue;
        }
    }

    (max_red, max_green, max_blue)
}

fn parse_handful(handful: &str) -> (i32,i32,i32) {
    let mut red: i32 = 0;
    let mut green: i32 = 0;
    let mut blue: i32 = 0;
    let colors = handful.split(",");
    for color in colors {
        let tokens: Vec<_> = color.split_whitespace().collect();
        let count = tokens[0].parse::<i32>().unwrap();
        let name = tokens[1];
        match name {
            "red" => red = count,
            "green" => green = count,
            "blue" => blue = count,
            _ => panic!("Invalid color: {}", color),
        }
    }

    (red, green, blue)
}

#[cfg(test)]
mod day2_tests {
    use super::*;

    #[test]
    fn test_parse_handful() {
        let input = "12 blue, 15 red, 2 green";
        assert_eq!(parse_handful(input), (15, 2, 12));
    }

    #[test]
    fn test_get_maxs_in_game() {
        let input = "Game 1: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red";
        assert_eq!(get_maxs_in_game(input), (17, 9, 17));
    }

    #[test]
    fn test_is_valid_game() {
        let input = "Game 1: 12 blue, 15 red, 2 green; 17 red, 8 green, 5 blue; 8 red, 17 blue; 9 green, 1 blue, 4 red";
        assert!(!is_valid_game(input));
    }

    #[test]
    fn test_solution_pt1() {
        let input = "day2/test.txt";
        assert_eq!(solution_pt1(input), 8);
    }
}
