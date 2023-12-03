use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use regex::Regex;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
} 

fn digit_from_string(inslice: &str) -> Option<u32> {
    // this regex came after the monstroity below
    let english_digits_regex = Regex::new(r"^(one|two|three|four|five|six|seven|eight|nine)").unwrap();
    match english_digits_regex.find(inslice) {
        None => return None,
        _ => ()
    };

    // one
    // t{wo, hree}
    // f{our, ive}
    // s{ix, even}
    // eight
    // nine
    // why did I choose to do it like this lol
    match inslice.chars().nth(0) {
        Some('o') => match &inslice[1..3] {
            "ne" => return Some(1),
            _ => return None
        },
        Some('t') => match &inslice[1..3] {
            "wo" => return Some(2),
            "hr" => match &inslice[3..5] {
                "ee" => return Some(3),
                _ => return None
            },
            _ => return None
        },
        Some('f') => match &inslice[1..4] {
            "our" => return Some(4),
            "ive" => return Some(5),
            _ => return None
        },
        Some('s') => match &inslice[1..3] {
            "ix" => return Some(6),
            "ev" => match &inslice[3..5] {
                "en" => return Some(7),
                _ => return None
            },
            _ => return None
        },
        Some('e') => match &inslice[1..5] {
            "ight" => return Some(8),
            _ => return None
        },
        Some('n') => match &inslice[1..4] {
            "ine" => return Some(9),
            _ => return None
        },
        _ => None,
    }
}

fn main() {
    let mut total_count = 0;

    if let Ok(lines) = read_lines("./d1.input") {
        for line in lines {
            if let Ok(raw_calibration_value) = line {
                //println!("{}", raw_calibration_value);
                let mut first_digit = 0;
                let mut last_digit = 0;
                
                for (i, c) in raw_calibration_value.chars().enumerate() {
                    match c.to_digit(10) {
                        Some(d) => match first_digit {
                            0 => { first_digit = d; last_digit = d; },
                            _ => last_digit = d,
                        },
                        None => {
                            let d = digit_from_string(&raw_calibration_value[i..]);
                            match d {
                                Some(d2) => {
                                    match first_digit {
                                        0 => { first_digit = d2; last_digit = d2; },
                                        _ => last_digit = d2,
                                    }
                                },
                                None => (),
                            }
                        },
                    }
                }
                //println!("Found {first_digit}{last_digit} in line {raw_calibration_value}");
                let line_total = (first_digit * 10) + last_digit;
                //println!("{}", line_total);
                total_count += line_total;
            }
        }
    }

    println!("Total sum of all calibration values: {total_count}");
}