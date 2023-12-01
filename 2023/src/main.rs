fn main() -> i32 {
    println!("Hello, world!");
    5
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_main() {
        assert_eq!(main(), 5);
    }
}
