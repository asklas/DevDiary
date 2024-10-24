package org.example.kafkaproject.Service;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Service;

@Service
public class TodoConsumer {

    @KafkaListener(topics = "todo",groupId = "todo_group")
    public void listen(String message) {
        System.out.println(message);
    }
}
