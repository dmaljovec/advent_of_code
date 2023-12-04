pub fn parse_file(file_name: &str) -> Vec<String> {
    let contents = std::fs::read_to_string(file_name)
        .expect("Something went wrong reading the file")
        .lines().map(String::from).collect();
    contents
}


#[cfg(test)]
mod utils_tests {
    use super::*;

    #[test]
    fn test_parse_file() {
        let input = "day1/test.txt";
        assert_eq!(parse_file(input), ["abcd","efgh"]);
    }

}
