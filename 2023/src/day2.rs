use regex::Regex;

const RED_COUNT = 12;
const GREEN_COUNT = 13;
const BLUE_COUNT = 14;

pub fn solution_pt1(input: &str) -> i32 {
    0
}

pub fn solution_pt2(input: &str) -> i32 {
    0
}

fn parse_line(line: &str) -> Vec<(i32,i32,i32)> {
    let mut max_red = 0;
    let mut max_green = 0;
    let mut max_blue = 0;
    let handfuls = line.split(":")[1].split(";");

    (max_red, max_green, max_blue)
}

fn parse_handful(handful: &str) -> (i32,i32,i32) {
    let mut red = 0;
    let mut green = 0;
    let mut blue = 0;
    let colors = handful.split(",");

    (red, green, blue)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_handful() {
        let input = "12 blue, 15 red, 2 green";
        assert_eq!(parse_handful(input), (15, 2, 12));
    }
}
