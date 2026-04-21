import csv


def process_grades():
    try:
        with open("grades.csv", "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            # grades_list = list(reader)
            # print(grades_list)
            # 使用推导式 + 异常处理过滤有效数据
            valid_grades = []
            for row in reader:
                try:
                    math = int(row["数学"])
                    english = int(row["英语"])
                    chinese = int(row["语文"])
                    mark = row["备注"]
                    valid_grades.append(
                        {
                            "name": row["姓名"],
                            "math": math,
                            "english": english,
                            "chinese": chinese,
                            "mark": mark,
                            "total": math + english + chinese,
                        }
                    )

                except (ValueError, KeyError):
                    print(
                        f"数据异常: {row['姓名']} 数学、英语、语文成绩不是整数或备注为空，过滤无效数据"
                    )
                    continue
        # 计算各科平均分
        if len(valid_grades) > 0:
            avg_math = sum(s["math"] for s in valid_grades) / len(valid_grades)
            avg_english = sum(s["english"] for s in valid_grades) / len(valid_grades)
            avg_chinese = sum(s["chinese"] for s in valid_grades) / len(valid_grades)
            print(f"有效数据数量: {len(valid_grades)}")
            print(
                f"数学平均分: {avg_math:.2f}, 英语平均分: {avg_english:.2f}, 语文平均分: {avg_chinese:.2f}"
            )  # .2f 保留两位小数
        else:
            print("没有有效数据，无法计算平均分")

        # 写入结果文件
        with open("grades_result_summary.txt", "w", encoding="utf-8") as f:
            f.write("====== 成绩统计摘要 ======\n")
            f.write(f"总人数: {len(valid_grades)}\n")
            f.write(f"数学平均分: {avg_math:.2f}\n")
            f.write(f"英语平均分: {avg_english:.2f}\n")
            f.write(f"语文平均分: {avg_chinese:.2f}\n")

            # 总分大于270的人数
            high_score_count = [s["name"] for s in valid_grades if s["total"] > 270]
            print(high_score_count)
            f.write(f"优秀学生(成绩高于270分): {', '.join(high_score_count)}\n")
            # 打印所有有效成绩
            f.write("所有有效成绩:\n")
            for student in valid_grades:
                f.write(
                    f"{student['name']} 数学: {student['math']} 英语: {student['english']} 语文: {student['chinese']} 总分: {student['total']}\n"
                )
        print("成绩统计摘要已写入 grades_result_summary.txt 文件")
    except FileNotFoundError:
        print("grades.csv 文件不存在，请先创建数据文件")
    except Exception as e:
        print(f"程序执行出错: {e}")


if __name__ == "__main__":
    process_grades()
