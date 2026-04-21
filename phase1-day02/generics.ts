// Day 2: TypeScript Generics + Utility Types

// 1. 泛型基础
function identity<T>(arg: T): T {
    return arg;
}

console.log(identity<string>("前端转 AI"));
console.log(identity<number>(2));

// 2. 泛型接口
interface Developer<T = string> {
    name: string;
    experience: number;
    skills: T[];           // 泛型数组
    extraInfo?: T;
}

const frontendDev: Developer<string> = {
    name: "Cazuuya",
    experience: 5,
    skills: ["React", "TypeScript", "Tailwind"],
};

const aiDev: Developer<number> = {
    name: "小明",
    experience: 4,
    skills: ["Python", "FastAPI"],
    extraInfo: 90,   // 学习进度百分比
};

// 3. Utility Types 实战
type BaseProject = {
    id: number;
    title: string;
    status: "todo" | "in-progress" | "done";
    createdAt: Date;
};

// 只取部分字段
type ProjectSummary = Pick<BaseProject, "title" | "status">;

// 省略某些字段
type CreateProject = Omit<BaseProject, "id" | "createdAt">;

// 所有字段可选
type UpdateProject = Partial<BaseProject>;

// 只读版本
type ReadonlyProject = Readonly<BaseProject>;

// Record 示例（常用于映射）
type SkillLevel = Record<string, "beginner" | "intermediate" | "advanced">;

const mySkills: SkillLevel = {
    "React": "advanced",
    "Python": "beginner",
    "LangChain": "beginner"
};

// ==================== 测试 ====================
console.log("Frontend Dev:", frontendDev);
console.log("AI Dev:", aiDev);
console.log("Project Summary Type:", { title: "AI 聊天机器人", status: "in-progress" } as ProjectSummary);