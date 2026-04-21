// Day 3: TypeScript Decorators + 类型守卫

// 1. 装饰器示例
function log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
        console.log(`🚀 调用方法: ${propertyKey}，参数:`, args);
        const result = originalMethod.apply(this, args);
        console.log(`✅ 方法 ${propertyKey} 执行完成，结果:`, result);
        return result;
    };
    
    return descriptor;
}

function validateAIInput(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
    const originalMethod = descriptor.value;
    
    descriptor.value = function (...args: any[]) {
        if (args[0] && typeof args[0] === 'number' && args[0] < 1) {
            console.warn("⚠️  警告：学习天数不能小于 1，已自动修正为 1");
            args[0] = 1;
        }
        return originalMethod.apply(this, args);
    };
}

// 2. 类型守卫
type LearningPhase = "Phase1" | "Phase2" | "Phase3";

function isAdvancedPhase(phase: LearningPhase): phase is "Phase3" {
    return phase === "Phase3";
}

function printPhaseInfo(phase: LearningPhase) {
    if (isAdvancedPhase(phase)) {
        console.log("🎯 你已进入高级 Agent 开发阶段！");
    } else {
        console.log(`📚 当前阶段: ${phase}，继续加油！`);
    }
}

// 3. 使用装饰器的类
class AiLearningTracker {
    private progress: number = 0;

    @log
    @validateAIInput
    learn(day: number): string {
        this.progress += day * 5;
        return `Day ${day} 学习完成，当前总进度: ${this.progress}%`;
    }
}

// ==================== 测试 ====================
const tracker = new AiLearningTracker();

console.log(tracker.learn(3));
console.log(tracker.learn(0));   // 测试装饰器校验

printPhaseInfo("Phase1");
printPhaseInfo("Phase3");