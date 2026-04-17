# 学生成绩管理系统（字典 + 列表 + 函数 + 控制路）
import json
import os

# 文件路径
DATA_FILE = "phase1-day01/students.json"

student = {}  # 全局字典: {学号:{"name":姓名,"score":[语文,数学,英语]}}


def loa_data():
    """从文件加载学生数据"""
    global student
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                student = json.load(f)
                print(f"✅ 已从文件加载 {len(student)} 名学生数据")
        except json.JSONDecodeError:
            print("文件内容格式错误")
            student = {}
        except Exception as e:
            print(f"⚠️ 加载数据失败: {e}，将使用空数据")
            student = {}
        else:
            print("📁 未找到数据文件，将从零开始")


def save_data():
    """将学生数据保存到文件"""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(student, f, ensure_ascii=False, indent=4)
            print(f"✅ 已将 {len(student)} 名学生数据保存到文件 {DATA_FILE}")
    except Exception as e:
        print(f"⚠️ 保存数据失败: {e}")


def add_student():
    # 添加学生
    print("添加学生")
    id = input("请输入学号：")
    if id in student:
        print("学号已存在，请重新输入")
        return
    name = input("请输入姓名：")
    scores = []
    for subject in ["语文", "数学", "英语"]:
        while True:
            try:
                score = float(input(f"请输入{subject}成绩："))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("成绩必须在0-100之间")
            except ValueError:
                print("请输入数字")
    # score = [float(input("请输入语文成绩：")), float(input("请输入数学成绩：")), float(input("请输入英语成绩："))]
    student[id] = {"name": name, "score": scores}
    save_data()
    print("添加成功")


# 查询学生
def query_student():
    # 查询学生
    print("查询学生")
    id = input("请输入学号：")
    if id not in student:
        print("学号不存在，请重新输入")
        return
    # 打印学生信息
    print(f"{id}的姓名是{student[id]['name']}，成绩是{student[id]['score']}")
    # 计算平均成绩
    avg = sum(student[id]["score"]) / len(student[id]["score"])
    print(f"{id}的平均成绩是{avg:.2f}")


def modify_score():
    # 修改学生成绩
    print("修改学生成绩")
    id = input("请输入学号：")
    if id not in student:
        print("学号不存在，请重新输入")
        return
    for i, subject in enumerate(["语文", "数学", "英语"]):
        while True:
            try:
                score = float(input(f"请输入{subject}成绩："))
                if 0 <= score <= 100:
                    student[id]["score"][i] = score
                    break
                else:
                    print("成绩必须在0-100之间")
            except ValueError:
                print("请输入数字")
    save_data()
    print("修改成功")


def delete_student():
    # 删除学生
    print("删除学生")
    id = input("请输入学号：")
    if id not in student:
        print("学号不存在，请重新输入")
        return
    del student[id]
    save_data()
    print("删除成功")


def show_all_students():
    # 显示所有学生
    print("显示所有学生")
    if not student:
        print("当前没有学生")
        return
    for id, info in student.items():
        print(f"{id}的姓名是{info['name']}，成绩是{info['score']}")


def main():
    while True:
        print("1. 添加学生")
        print("2. 查询学生")
        print("3. 修改学生成绩")
        print("4. 删除学生")
        print("5. 显示所有学生")
        print("6. 退出系统")
        choice = input("请输入您的选择(1-6)：")
        if choice == "1":
            add_student()
        elif choice == "2":
            query_student()
        elif choice == "3":
            modify_score()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            show_all_students()
        elif choice == "6":
            break
        else:
            print("无效的选择，请重新输入")


if __name__ == "__main__":
    main()
