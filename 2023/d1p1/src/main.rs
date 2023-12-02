use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
} 

fn main() {
    let mut total_count = 0;

    if let Ok(lines) = read_lines("./d1p1.input") {
        for line in lines {
            if let Ok(raw_calibration_value) = line {
                //println!("{}", raw_calibration_value);
                let mut first_digit = 0;
                let mut last_digit = 0;
                
                for c in raw_calibration_value.chars() {
                    match c.to_digit(10) {
                        Some(d) => match first_digit {
                            0 => {first_digit = d; last_digit = d;},
                            _ => last_digit = d,
                        },
                        None => (),
                    }
                }
                let line_total = (first_digit * 10) + last_digit;
                //println!("{}", line_total);
                total_count += line_total;
            }
        }
    }

    println!("Total sum of all calibration values: {total_count}");
}