#!/usr/bin/env python3
"""
Portfolio Website Setup Script
Initializes the database and optionally creates sample blog posts.
"""

from app import app, db, BlogPost
from datetime import datetime, timedelta

def create_sample_posts():
    """Create sample blog posts for demonstration"""
    sample_posts = [
        {
            "title": "Migrating from AWS Elastic Beanstalk to Kubernetes: Lessons Learned",
            "content": """Recently, I led a major infrastructure migration project at CSG International where we moved our production workloads from AWS Elastic Beanstalk to Amazon EKS (Kubernetes). This was a complex undertaking that resulted in 75% faster deployments and zero downtime during the transition.

The Challenge
Our existing infrastructure was becoming a bottleneck. Deployments were slow, scaling was limited, and we needed more control over our container orchestration. The decision to move to Kubernetes was driven by several factors:

1. Better resource utilization
2. Improved scaling capabilities  
3. Enhanced monitoring and observability
4. More flexible deployment strategies

The Migration Process
The migration involved several key steps:

Container Preparation: First, we containerized all our applications using Docker, ensuring they followed the 12-factor app principles.

EKS Cluster Setup: We provisioned new EKS clusters using Terraform, implementing proper networking, security groups, and IAM roles.

Gradual Migration: Instead of a big-bang approach, we migrated services one by one, allowing us to learn and adapt our process.

Monitoring Implementation: We set up comprehensive monitoring using Prometheus and Grafana to ensure visibility into our new infrastructure.

Results
The results exceeded our expectations:
- Deployment time reduced from 45 minutes to 10 minutes
- Zero downtime during the migration
- 40% improvement in resource utilization
- Better developer experience with GitLab CI/CD integration

This project reinforced the importance of careful planning, incremental changes, and robust monitoring in infrastructure migrations.""",
            "date_posted": datetime.utcnow() - timedelta(days=5)
        },
        {
            "title": "Cost Optimization with AWS Lambda: Automating EC2 Lifecycle Management",
            "content": """One of the most impactful projects I've worked on was developing an automated cost optimization solution that reduced our AWS bill by 30%. The solution uses Python and AWS Lambda to intelligently manage EC2 instance lifecycles in non-production environments.

The Problem
Like many organizations, we had development and testing environments running 24/7, even when no one was using them. This was costing us thousands of dollars monthly in unnecessary compute charges.

The Solution
I developed a serverless solution using AWS Lambda that:

1. Tags Analysis: Scans EC2 instances for specific tags that indicate environment type
2. Schedule Management: Uses CloudWatch Events to trigger start/stop actions based on predefined schedules
3. Smart Logic: Implements business rules to avoid stopping critical services
4. Reporting: Sends daily reports showing cost savings and instance status

Technical Implementation
The solution consists of several components:

Lambda Functions: Two main functions - one for stopping instances in the evening and another for starting them in the morning.

CloudWatch Events: Cron-based triggers that run the Lambda functions on schedule.

IAM Roles: Properly scoped permissions that allow the Lambda functions to manage EC2 instances securely.

SNS Integration: Sends notifications when instances are started/stopped or when errors occur.

Key Features
- Automatic detection of non-production environments
- Flexible scheduling based on instance tags
- Cost reporting and analytics
- Error handling and notification system
- Dry-run mode for testing changes

Results
After implementing this solution:
- 30% reduction in overall AWS costs
- $50,000+ annual savings
- Zero manual intervention required
- Improved cost visibility across teams

The project demonstrates how small automation efforts can have significant business impact when applied thoughtfully to cloud infrastructure management.""",
            "date_posted": datetime.utcnow() - timedelta(days=12)
        },
        {
            "title": "Infrastructure as Code Best Practices: From Terraform to Terragrunt",
            "content": """During my time at CSG International, I led the refactoring of our infrastructure codebase from Terraform workspaces to Terragrunt. This migration improved code reusability by 85% and reduced deployment times by 60%.

Why Terragrunt?
While Terraform is powerful, managing multiple environments and maintaining DRY (Don't Repeat Yourself) principles can be challenging with vanilla Terraform. Terragrunt addresses these challenges by:

1. Eliminating code duplication across environments
2. Providing better backend configuration management
3. Enabling more flexible module composition
4. Offering enhanced state management

Migration Strategy
The migration was planned in phases:

Phase 1: Analysis and Planning
- Audited existing Terraform codebase
- Identified common patterns and duplication
- Designed the new Terragrunt structure

Phase 2: Module Development
- Created reusable Terraform modules
- Implemented proper variable interfaces
- Added comprehensive documentation

Phase 3: Terragrunt Implementation
- Converted workspace-based code to Terragrunt
- Implemented environment-specific configurations
- Set up proper dependency management

Phase 4: Testing and Validation
- Extensive testing in development environments
- Gradual rollout to staging and production
- Performance monitoring and optimization

Key Improvements
The new architecture provided several benefits:

Code Reusability: Modules can be shared across projects and environments with different configurations.

Maintainability: Changes to infrastructure patterns can be made in one place and propagated across environments.

Consistency: All environments follow the same patterns, reducing configuration drift.

Scalability: Adding new environments or services is much faster and less error-prone.

Best Practices Learned
Through this project, I developed several best practices:

1. Module Design: Keep modules focused and composable
2. Variable Management: Use clear naming conventions and proper defaults
3. State Management: Implement proper state isolation and locking
4. Documentation: Maintain comprehensive module documentation
5. Testing: Use tools like Terratest for infrastructure testing

The success of this migration has made infrastructure management much more efficient and has set a solid foundation for future growth.""",
            "date_posted": datetime.utcnow() - timedelta(days=20)
        }
    ]
    
    for post_data in sample_posts:
        existing_post = BlogPost.query.filter_by(title=post_data["title"]).first()
        if not existing_post:
            post = BlogPost(
                title=post_data["title"],
                content=post_data["content"],
                date_posted=post_data["date_posted"]
            )
            db.session.add(post)
    
    db.session.commit()
    print(f"✅ Created {len(sample_posts)} sample blog posts!")

def setup_database():
    """Initialize the database and create sample data"""
    print("🔧 Setting up database...")
    
    with app.app_context():
        # Create all tables
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Create sample blog posts
        create_sample_posts()
        
        print("🎉 Database setup complete!")

def main():
    """Main setup function"""
    print("🚀 Setting up Portfolio Website...")
    print("=" * 50)
    
    try:
        setup_database()
        print("\n🌟 Setup completed successfully!")
        print("📝 Run 'python run.py' to start the website")
        print("🌐 Visit http://localhost:5000 to see your portfolio")
    except Exception as e:
        print(f"❌ Error during setup: {e}")
        return False
    
    return True

if __name__ == '__main__':
    main()