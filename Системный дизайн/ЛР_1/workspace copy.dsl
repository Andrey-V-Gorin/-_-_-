workspace {
    name "CoinKeeper"
    description "Правильные финансовые решения каждый день"

    # включаем режим с иерархической системой идентификаторов
    !identifiers hierarchical

    model {

        u1 = person "Пользователь"
        
        s1 = softwareSystem "CoinKeeper" {
        
            db = container "Database" {
                technology "PostgreSQL 14"
            }

            subject = container "Пользователь" {
                technology "Java Spring"
                -> db "Сохранение и получение информации о пользователе" "JDBC"
            }

            content = container "Доход-Расход" {
                technology "Java Spring"
                -> db "Cохранение и получение информации о планируемом доходе/расходе" "JDBC"
            }

            Analytical_module = container "Analytical module" {
                technology "low-code"
                -> content "Получение информации о планируемом доходе/расходе" "low-code"
            }

            be = container "API Gateway" {
                -> subject "Создание/удаление нового пользователя" "HTTPS"
                -> content "Создание/удаление информации о планируемом доходе/расходе" "HTTPS"
                -> Analytical_module "Посчитать динамику бюджета за период" "HTTPS"
                technology "Java Spring Cloud Gateway"

                c1 = component "Single Sign On" {

                }
                
                c2 = component "Logging Adpater" {

                }
            }
            fe = container "Single Page Application" {
                technology "JS, React"
                -> be "Получение/изменение данных" "HTTPS"
            }
        }

        u1 -> s1.fe "Поиск пользователя по логину"
        u1 -> s1.fe "Поиск пользователя по маске имя и фамилия"
        u1 -> s1.fe "Получить перечень планируемых доходов/расходов"
        u1 -> s1.fe "Загрузить перечень планируемых доходов/расходов"
        u1 -> s1.fe "Получить данные о динамике бюджета за период"

        u1 -> s1 "Загружает доходы/расходы, получает данные о доходах/расходах, получает данные о динамике бюджета за период"
        

        deploymentEnvironment "Production" {

            deploymentNode "DMZ" {
                deploymentNode "NGinx Server" {
                    containerInstance s1.fe
                    instances 2
                }
            }

            deploymentNode "Inside" {

                in_db = infrastructureNode "Backup Database Server" 
                dn_db = deploymentNode "Database Server" {
                 containerInstance s1.db
                 -> in_db "Backup"
                }

                deploymentNode "k8s pod backend" {
                 containerInstance s1.be
                 instances 4
                }

                deploymentNode "k8s pod subject" {
                    containerInstance s1.subject
                }

                deploymentNode "k8s pod content" {
                    containerInstance s1.content
                }

                deploymentNode "k8s pod Analytical_modulet" {
                    containerInstance s1.Analytical_module
                }         

            }

        }
        
    }

    views {

        dynamic s1 "uc01" "Создание нового пользователя" {
            autoLayout lr

            u1 -> s1.fe "Открыть страницу"
            s1.fe -> s1.be "POST /subject/{id}"
            s1.be -> s1.subject "POST /subject/{id}"
            s1.subject -> s1.db "INSERT INTO subject (...) VALUES (...)"
        }

        dynamic s1 "uc02" "Поиск пользователя по логину" {
            autoLayout lr

            u1 -> s1.fe "Открыть страницу пользователя"
            s1.fe -> s1.be "GET /subject/{logi}"
            s1.be -> s1.subject "GET /subject/{logi}"
            s1.subject -> s1.db "SELECT * FROM subject WHERE id={logi}"
        }

        dynamic s1 "uc03" "Поиск пользователя по маске имя и фамилии" {
            autoLayout lr

            u1 -> s1.fe "Открыть страницу пользователя"
            s1.fe -> s1.be "GET /subject/{mask}"
            s1.be -> s1.subject "GET /subject/{mask}"
            s1.subject -> s1.db "SELECT * FROM subject WHERE id={mask}"
        }

        dynamic s1 "uc04" "Создать планируемый доход/расход" {
            autoLayout lr

            u1 -> s1.fe "Открыть страницу пользователя"
            s1.fe -> s1.be "GET /subject/{id}"
            s1.be -> s1.subject "GET /subject/{id}"
            s1.subject -> s1.db "SELECT * FROM subject WHERE id={id}"

            u1 -> s1.fe "Создать планируемый доход/расход"
            s1.fe -> s1.be "POST /content/{id}"
            s1.be -> s1.content "POST /content/{id}"
            s1.content -> s1.db "INSERT INTO  content (...) VALUES (...)"
        }

        dynamic s1 "uc05" "Получить перечень планируемых доходов/расходов" {
            autoLayout lr

            u1 -> s1.fe "Открыть страницу пользователя"
            s1.fe -> s1.be "GET /subject/{id}"
            s1.be -> s1.subject "GET /subject/{id}"
            s1.subject -> s1.db "SELECT * FROM subject WHERE id={id}"

            u1 -> s1.fe "Получить перечень планируемых доходов/расходов"
            s1.fe -> s1.be "GET /content/{id}"
            s1.be -> s1.content "GET /content/{id}"
            s1.content -> s1.db "SELECT * FROM content WHERE id={id}"
        }

        dynamic s1 "uc06" "Посчитать динамику бюджета за период" {
            autoLayout lr

            u1 -> s1.fe "Открыть страницу пользователя"
            s1.fe -> s1.be "GET /subject/{id}"
            s1.be -> s1.subject "GET /subject/{id}"
            s1.subject -> s1.db "SELECT * FROM subject WHERE id={id}"

            u1 -> s1.fe "Посчитать динамику бюджета за период"
            s1.fe -> s1.be "GET /Analytical_datа/{id}"
            s1.be -> s1.Analytical_module "GET /Analytical_datа/{id}"
            s1.Analytical_module -> s1.content "GET /content/{id}"
            s1.content -> s1.db "SELECT * FROM content WHERE id={id}"
        }

        themes default
        systemContext s1 {
            include *
            autoLayout
        }

        container s1 "vertical" {
            include *
            autoLayout
        }

        container s1 "hotizontal" {
            include *
            autoLayout lr
        }

        component s1.be {
            include *
            autoLayout lr
        }

        deployment * "Production" {
            include *
            autoLayout

        }
    }
}