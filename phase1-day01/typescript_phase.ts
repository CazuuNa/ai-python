// Day 1 TypeScript 高级类型复习

// 1. type 与 interface
type UserRole = "frontend" | "ai-engineer" | "fullstack";

// Intersection 类型（合并多个类型）
type BaseInfo = {
  name: string;
  experience: number;
};

type AiSkills = {
  pythonLevel: "beginner" | "intermediate";
  knowsFastAPI: boolean;
};

type Developer = BaseInfo & AiSkills;   // Intersection

// Union 类型
type LearningPhase = "Phase1" | "Phase2" | "Phase3";

const currentDev: Developer = {
  name: "Cazuuya",
  experience: 5,
  pythonLevel: "beginner",
  knowsFastAPI: false,
};

// 类型守卫函数
function isAiEngineer(dev: Developer): boolean {
  return dev.pythonLevel === "intermediate" || dev.knowsFastAPI;
}

console.log(`开发者: ${currentDev.name}`);
console.log(`当前阶段: Phase1`);
console.log(`是否具备 AI 工程师潜力: ${isAiEngineer(currentDev)}`);

// 泛型简单预习（后续会大量用到）
function logProgress<T>(day: number, progress: T): void {
  console.log(`Day ${day} 进度: ${progress}`);
}

logProgress(1, "Python 基础 + TS 类型复习");