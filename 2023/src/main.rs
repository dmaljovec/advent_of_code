use regex::Regex;

fn main() {
    println!("{}", solution("day1/input.txt"));
    println!("{}", solution_pt2("day1/input.txt"));
}

fn solution(input: &str) -> i32 {
    parse_file(input).iter()
    .map(get_number)
    .sum()
}

fn solution_pt2(input: &str) -> i32 {
    parse_file(input).iter()
    .map(get_number_pt2)
    .sum()
}

fn parse_file(file_name: &str) -> Vec<String> {
    let contents = std::fs::read_to_string(file_name)
        .expect("Something went wrong reading the file")
        .lines().map(String::from).collect();
    contents
}

fn translate(number: &str) -> i32 {
    match number {
        "one" | "eno" => 1,
        "two" | "owt" => 2,
        "three" | "eerht" => 3,
        "four" | "ruof" => 4,
        "five" | "evif" => 5,
        "six" | "xis" => 6,
        "seven" | "neves" => 7,
        "eight" | "thgie" => 8,
        "nine" | "enin" => 9,
        _ => number.parse::<i32>().unwrap(),
    }
}

fn get_number(line: &String) -> i32 {
    let re = Regex::new(r"\d")
        .expect("Invalid Regex");
    let matches: Vec<regex::Match> = re.find_iter(line).collect();
    let digits = format!("{}{}", matches.first().unwrap().as_str(), matches.last().unwrap().as_str());
    digits.parse::<i32>().unwrap()
}

fn get_number_pt2(line: &String) -> i32 {
    let re = Regex::new(r"\d|one|two|three|four|five|six|seven|eight|nine").expect("Invalid Regex");
    let backwards = Regex::new(r"\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin").expect("Invalid Regex");
    
    let reversed_line = line.chars().rev().collect::<String>();

    let first = translate(re.find(line).unwrap().as_str());
    let last = translate(backwards.find(&reversed_line).unwrap().as_str());

    let digits = format!("{}{}", first, last);
    let result = digits.parse::<i32>().unwrap();
    // println!("{}: {}", result, line);
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_file() {
        let input = "day1/test.txt";
        assert_eq!(parse_file(input), ["abcd","efgh"]);
    }

    #[test]
    fn test_solution() {
        let input = "day1/part_1.txt";
        assert_eq!(solution(input), 142);
    }
    
    #[test]
    fn test_get_number() {
        let input = String::from("1abc2");
        assert_eq!(get_number(&input), 12);
    }
    
    #[test]
    fn test_get_number_pt2_a() {
        let input = String::from("1six15ninebgnzhtbmlxpnrqoneightfhp");
        assert_eq!(get_number_pt2(&input), 18);
    }

    #[test]
    fn test_get_number_pt2() {
        let input = String::from("oneabc2");
        assert_eq!(get_number_pt2(&input), 12);
    }
    
    #[test]
    fn test_solution_pt2() {
        let input = "day1/part_2.txt";
        assert_eq!(solution_pt2(&input), 281);
    }
}
