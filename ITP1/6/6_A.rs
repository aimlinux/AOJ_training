use std::io;

fn main() {
    // 1行目（数列の長さ n）は読み込むだけで今回は特に使わない
    let mut n_str = String::new();
    io::stdin().read_line(&mut n_str).unwrap();

    // 2行目（数列の本体）を読み込む
    let mut a_str = String::new();
    io::stdin().read_line(&mut a_str).unwrap();

    // 空白で分割し、ベクタ（配列）に格納
    let a: Vec<&str> = a_str.trim().split_whitespace().collect();

    // イテレータを逆順(.rev)にし、空白で結合(.join)して出力
    let reversed: Vec<&str> = a.into_iter().rev().collect();
    println!("{}", reversed.join(" "));
}