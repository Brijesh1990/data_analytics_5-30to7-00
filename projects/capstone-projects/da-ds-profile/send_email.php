<?php
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require 'vendor/autoload.php';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Check if the form arrays are set
    $name = isset($_POST['name']) ? htmlspecialchars(trim($_POST['name'])) : '';
    $email = isset($_POST['email']) ? htmlspecialchars(trim($_POST['email'])) : '';
    $message = isset($_POST['message']) ? htmlspecialchars(trim($_POST['message'])) : '';

    // Basic Validation
    if (empty($name) || empty($email) || empty($message)) {
        echo "<script>alert('Please fill out all required fields.'); window.history.back();</script>";
        exit;
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "<script>alert('Invalid email format.'); window.history.back();</script>";
        exit;
    }

    // Create an instance; passing `true` enables exceptions
    $mail = new PHPMailer(true);

    try {
        // --- Server settings ---
        $mail->isSMTP();
        // TODO: Replace with your actual SMTP details
        $mail->Host = 'smtp.gmail.com';                       // Set the SMTP server to send through (e.g. smtp.gmail.com)
        $mail->SMTPAuth = true;                                   // Enable SMTP authentication
        $mail->Username = 'brijeshpandey.tops@gmail.com';                 // SMTP username (your email)
        $mail->Password = 'yrjv onoi kksi xlvw';                    // SMTP app password
        $mail->SMTPSecure = "TLS";            // Enable implicit TLS encryption (SSL)
        $mail->Port = 587;                                    // TCP port to connect to; use 587 if you rely on STARTTLS

        // --- Recipients ---
        // Sending from the authenticated address. You can set the "From" name to the form submitter's name.
        $mail->setFrom('brijeshpandey.tops@gmail.com', "Portfolio Contact - {$name}");

        // This is where you will receive the message
        $mail->addAddress('brijeshpandey.tops@gmail.com', 'Brijesh Pandey');

        // Add the submitter's email as the Reply-To address
        $mail->addReplyTo($email, $name);

        // --- Content ---
        $mail->isHTML(true);

        // --- 1. Admin Notification Email (Sent to You) ---
        $mail->Subject = '🚨 New Portfolio Inquiry from: ' . $name;
        $mail->Body = '
        <div style="font-family: \'Inter\', Arial, sans-serif; max-width: 600px; margin: auto; padding: 30px; border-radius: 12px; background-color: #f8fafc; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <div style="text-align: center; margin-bottom: 25px;">
                <img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjRzMWlqdGQ5bnhvOXBvYjR0OXhhdmUwdXZtbG1zZ2Nuc215anR1ciZlcD12MV9pbnRlcm5hbF9naWZzX2dpZklkJmN0PWc/3o7WIurliOOxvKzZKg/giphy.gif" alt="New Inquiry" style="width: 100%; max-width: 300px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1);">
            </div>
            <h2 style="color: #1e293b; text-align: center; font-size: 24px; margin-bottom: 20px;">📫 New Contact Request</h2>
            <p style="color: #64748b; font-size: 15px; text-align: center; margin-bottom: 25px;">You received a new message from your portfolio website.</p>
            
            <div style="background-color: #ffffff; padding: 20px; border-radius: 8px; border-left: 4px solid #2563eb; margin-bottom: 25px; box-shadow: 0 2px 4px rgba(0,0,0,0.02);">
                <table style="width: 100%; border-collapse: collapse;">
                    <tr>
                        <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; width: 30%; color: #64748b; font-weight: bold;">Name:</td>
                        <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #0f172a;">' . $name . '</td>
                    </tr>
                    <tr>
                        <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #64748b; font-weight: bold;">Email:</td>
                        <td style="padding: 10px 0; border-bottom: 1px solid #f1f5f9; color: #0f172a;"><a href="mailto:' . $email . '" style="color: #2563eb; text-decoration: none;">' . $email . '</a></td>
                    </tr>
                    <tr>
                        <td style="padding: 15px 0 5px 0; color: #64748b; font-weight: bold;" colspan="2">Message:</td>
                    </tr>
                    <tr>
                        <td colspan="2" style="padding-top: 5px; color: #334155; line-height: 1.6;">' . nl2br($message) . '</td>
                    </tr>
                </table>
            </div>
            
            <div style="text-align: center; margin-top: 30px;">
                <a href="mailto:' . $email . '" style="background-color: #2563eb; color: #ffffff; padding: 12px 25px; text-decoration: none; border-radius: 6px; font-weight: bold; font-size: 14px; display: inline-block;">Reply to ' . $name . '</a>
            </div>
        </div>';
        $mail->AltBody = "New Message from Portfolio Contact Form\n\nName: {$name}\nEmail: {$email}\nMessage:\n{$message}";

        // Send the notification to Brijesh
        $mail->send();

        // --- 2. Client Auto-Responder Email (Sent to the User) ---
        $mail->clearAllRecipients(); // Remove Brijesh from the To: field
        $mail->clearReplyTos(); // Clear old Reply-To

        // Send TO the user who filled the form
        $mail->addAddress($email, $name);
        // User replies back to Brijesh
        $mail->addReplyTo('brijeshpandey.tops@gmail.com', 'Brijesh Pandey');

        $mail->Subject = 'Thanks for reaching out! Let\'s connect.';
        $mail->Body = '
        <div style="font-family: \'Inter\', Arial, sans-serif; max-width: 600px; margin: auto; padding: 30px; border-radius: 12px; background-color: #ffffff; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <div style="text-align: center; margin-bottom: 25px;">
                <img src="https://media.giphy.com/media/VbKnjQzZ80m2I/giphy.gif" alt="Data Science Hello" style="width: 100%; max-width: 350px; border-radius: 12px;">
            </div>
            <h2 style="color: #1e293b; text-align: center; font-size: 22px;">Hello ' . $name . ',<br><span style="color: #2563eb;">Thanks for reaching out!</span></h2>
            
            <p style="color: #475569; font-size: 15px; line-height: 1.6; text-align: center; margin-bottom: 30px;">
                I have warmly received your message and will be getting back to you as soon as I can to discuss your data needs and explore how we can work together.
            </p>
            
            <table style="width: 100%; background-color: #f8fafc; border-radius: 8px; padding: 20px; text-align: left;">
                <tr>
                    <td style="padding-bottom: 15px;">
                        <h3 style="margin: 0; color: #0f172a; font-size: 18px;">Brijesh Kumar Pandey</h3>
                        <p style="margin: 5px 0 0 0; color: #2563eb; font-weight: 500; font-size: 14px;">Data Analyst & Data Scientist</p>
                    </td>
                    <td style="text-align: right; padding-bottom: 15px;">
                        <a href="https://github.com/Brijesh1990" style="display: inline-block; background-color: #1e293b; color: #fff; padding: 8px 15px; border-radius: 6px; text-decoration: none; font-size: 12px; font-weight: bold;">View GitHub</a>
                    </td>
                </tr>
                <tr>
                    <td colspan="2" style="border-top: 1px solid #e2e8f0; padding-top: 15px; font-size: 13px; color: #64748b;">
                        📍 150 feet ring road Rajkot 36005 (Remote Okay)<br>
                        📧 <a href="mailto:brijeshpandey.tops@gmail.com" style="color: #2563eb; text-decoration: none;">brijeshpandey.tops@gmail.com</a>
                    </td>
                </tr>
            </table>
            
            <p style="color: #94a3b8; font-size: 12px; text-align: center; margin-top: 30px;">
                This is an automated confirmation that your message was safely delivered to my inbox.
            </p>
        </div>';
        $mail->AltBody = "Hello {$name},\n\nThank you for reaching out! I've warmly received your message and will be getting back to you as soon as I can to discuss your data needs and explore how we can work together.\n\nBest regards,\nBrijesh Kumar Pandey\nData Analyst & Data Scientist\nbrijeshpandey.tops@gmail.com";

        // Send auto-reply to the user
        $mail->send();

        // Success redirect
        echo "<script>alert('Message has been sent successfully!'); window.location.href = 'index.html#contact';</script>";
    } catch (Exception $e) {
        // Error handling
        echo "<script>alert('Message could not be sent. Mailer Error: {$mail->ErrorInfo}'); window.history.back();</script>";
    }
} else {
    // If it's not a POST request, redirect back to the site
    header("Location: index.html");
    exit;
}
