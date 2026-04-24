// ty--zod入门
/**
 * 核心知识
 * zod基础 z.string() z.number() z.boolean() z.array() z.object()
 * 验证和解析 .parse() .safeParse()
 * 错误处理 .catch()
 * 自定义验证 .refine()
 * 验证规则 .min() .max() .regex() .email() .url() .uuid() .ipv4() .ipv6()
 * 验证规则 .int() .float() .bool()
 * 验证规则 .array() .object()
 * 类型推断 z.infer<typeof schema>
 * 默认值和可选字段 .optional() .default()
 */

import { z } from 'zod';
// == 基础 Schema ==
const TodoCreateSchema = z.object({
    title: z
        .string()
        .min(1, '标题不能为空')
        .max(100, '标题最多100个字符')
        .transform(s => s.trim()), // 自动去掉首尾空格
    description: z.string().max(500).optional(), // 描述最多500个字符,可选
    completed: z.boolean().default(false), // 完成状态,默认false
    priority: z.number().int().min(1).max(5).default(1), // 优先级,默认1
    tags: z.array(z.string()).default([]), // 标签数组,默认空数组
});

// 类型推断：z.infer<typeof schema> 相当于interface TodoCreate {...}
type TodoCreate = z.infer<typeof TodoCreateSchema>;

// 对应py TodoUpdate (所有字段可选)
const TodoUpdateSchema = TodoCreateSchema.partial();
type TodoUpdate = z.infer<typeof TodoUpdateSchema>;

// 对应py TodoResponse
const TodoResponseSchema = TodoCreateSchema.extend({
    id: z.number().int().positive(), // 主键,整数,大于0
    created_at: z.date(), // 创建时间,日期时间
    updated_at: z.date(), // 更新时间,日期时间
});
type TodoResponse = z.infer<typeof TodoResponseSchema>;

// 使用Schema验证数据

function testValidation() {
    console.log('zod 验证测试');

    // 有效数据
    const validInput = {
        title: '  学习zod  ',
        description: '这是一个学习zod的示例',
        priority: 3,
        tags: ['typescript', 'validation'],
    };

    try {
        const todo = TodoCreateSchema.parse(validInput);
        console.log('有效数据解析成功');
        console.log('  - title:', todo.title); // 已自动 trim
        console.log('  - completed:', todo.completed); // 默认 false
        console.log('  - tags:', todo.tags);
    } catch (err) {
        console.error('解析失败:', err);
    }

    // 无效数据
    const invalidInput = {
        title: '',
        priority: 10, // 优先级超出范围
    };

    const result = TodoCreateSchema.safeParse(invalidInput);
    if (!result.success) {
        console.log(result.error.flatten().fieldErrors);
    }

    // 部分更新测试
    const updateInput = { completed: true };
    const updateResult = TodoUpdateSchema.safeParse(updateInput);
    if (updateResult.success) {
        console.log('\n✅ 部分更新数据有效:', updateResult.data);
    }
}

// 高级校验  自定义 refine
const UserSchema = z
    .object({
        username: z.string().min(2, '用户名至少2个字符'),
        email: z.string().email('请输入有效的邮箱地址'),
        password: z.string().min(6, '密码至少6个字符'),
        confirmPassword: z.string().min(6, '确认密码至少6个字符'),
    })
    .refine(data => data.password === data.confirmPassword, {
        message: '密码和确认密码不匹配',
        path: ['confirmPassword'],
    });

type User = z.infer<typeof UserSchema>;

function testUserValidation() {
    console.log('用户校验测试');
    const userInput = {
        username: 'cazuuya',
        email: 'test@example.com',
        password: '12345678',
        confirmPassword: '12345679', // 故意不一致
    };
    const userResult = UserSchema.safeParse(userInput);
    if (!userResult.success) {
        console.log(userResult.error.flatten().fieldErrors);
    }

    const correctInput = {...userInput, confirmPassword: '12345678'};
    const correctResult = UserSchema.safeParse(correctInput);
    if (correctResult.success) {
        console.log('\n✅ 正确数据有效:', correctResult.data);
    }
}

// 联合类型与 discriminated union
const SuccessResponseSchema = z.object({
    status:z.literal('success'),
    data:z.any(),
})

const ErrorResponseSchema = z.object({
    status:z.literal('error'),
    code:z.number()
    message:z.string(),
})

const ApiResponseSchema = z.discriminatedUnion('status',[
    SuccessResponseSchema,
    ErrorResponseSchema,
])

type ApiResponse = z.infer<typeof ApiResponseSchema>;

function testApiResponse(response: unknown) {
    console.log('ApiResponse 校验测试');
    const result = ApiResponseSchema.safeParse(response);
    if (!result.success) {
        console.log("响应格式无效");
        console.log(result.error.flatten().fieldErrors);
        return 
    }

    const resp = result.data
    if (resp.status === 'success') {
        console.log('成功响应:', resp.data);
    } else {
        console.log('错误响应:', resp);
    }
}

function testDiscriminatedUnion() {
    console.log('discriminated union 校验测试');
    handleApiResponse({
        status:'success',
        data:{id:1,title:'学习zod',completed:false},
    })
    handleApiResponse({
        status:'error',
        code:400,
        message:'请求参数错误',
    })
    handleApiResponse({
        status:'unknown',
    })
}

// AI Prompt Schema
const AIPromptSchema = z.object({
    role:z.enum(['system','user','assistant']),
    content: z.string(),
})

// type AIPrompt = z.infer<typeof AIPromptSchema>;

const ChatRequestSchema = z.object({
    messages:z.array(AIPromptSchema).min(1),
    temperature: z.number().min(0).max(2).default(0.7),
    maxTokens: z.number().int().positive().optional(),
    stream: z.boolean().default(false),
})

type ChatRequest = z.infer<typeof ChatRequestSchema>;

function testAIPrompt() {
    console.log('AI CHAT Request Schema');

    const request = {
        messages:[
            {role:'system',content:'你是一个专业的翻译'},
            {role:'user',content:'你好'},
            {role:'assistant',content:'你好！'},
        ],
        temperature:0.7,
    }

    const result = ChatRequestSchema.safeParse(request);
    if (result.success) {
        console.log("✅ AI 请求验证通过:");
        console.log("  - 消息数:", result.data.messages.length);
        console.log("  - 温度:", result.data.temperature);
        console.log("  - 流式:", result.data.stream);
    }
}

// ==================== 运行所有测试 ====================
testValidation();
testAdvancedValidation();
testDiscriminatedUnion();
testAIPrompt();
